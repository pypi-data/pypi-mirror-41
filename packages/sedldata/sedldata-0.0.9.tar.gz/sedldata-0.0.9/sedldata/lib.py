import datetime
import html
import json
import os
import getpass
import csv
from collections import OrderedDict
import io

import alembic.config
import jinja2
from flattentool import unflatten
import gspread
from gspread.utils import fill_gaps
from openpyxl import Workbook

from sedldata.database import Database


def in_notebook():
    if 'JPY_PARENT_PID' in os.environ:
        return True
    return False


def xl_to_json(infile, outfile):
    try:
        unflatten(
                input_name=infile,
                output_name=outfile,
                input_format='xlsx',
                metatab_name='Meta',
                metatab_vertical_orientation=True,
                root_list_path='deals',
                id_name='id',
                cell_source_map='sourcemap-' + outfile,
                root_id='')
        with open(outfile,'r') as json_file:
            data = json.load(json_file)
        with open('sourcemap-' + outfile,'r') as source_map:
            source_map_data = json.load(source_map)
    except Exception as e:
        raise e

    return data, source_map_data

table = jinja2.Template(
'''
<table class="dataframe">
    <thead>
    <tr>
      {% for header in headers %}
        <th style="text-align: left; vertical-align: top">{{ header }}</th>
      {% endfor %}
    </tr>
    </thead>
    <tbody>
      {% for row in data %}
        <tr>
          {% for cell in row %}
              <td style="text-align: left; vertical-align: top">
                {% if not display_full_json %}
                    <pre>{{ cell|truncate(50) }}</pre>
                {% else %}
                    <pre>{{ cell }}</pre>
                {% endif %}
              </td>
          {% endfor %}
        </tr>
      {% endfor %}
    </tbody>
</table>
'''
)


def generate_rows(result, limit, to_html=False):
    for num, row in enumerate(result):
        if num == limit:
            break
        if to_html:
            yield [json.dumps(item, indent=2) if isinstance(item, dict) else html.escape(str(item)) for item in row]
        else:
            yield [item for item in row]


class Session:

    def __init__(self, db_uri=None):
        if in_notebook():
            if not db_uri:
                db_uri = 'postgresql://sedldata:{password}@46.43.2.250:5432/sedldata'
            if '{password}' in db_uri:
                db_uri = db_uri.format(password=getpass.getpass("Enter database password:  "))
            self.db = Database(db_uri)
            self.db.upgrade()
        else:
            self.db = Database()

        self.gspread_client = None

    def get_gspread_client(self):
        if not self.gspread_client:
            from google.colab import auth
            from oauth2client.client import GoogleCredentials
            auth.authenticate_user()
            self.gspread_client = gspread.authorize(GoogleCredentials.get_application_default())
        return self.gspread_client

    def load_xlsx(self, collection=None, infile=None, outfile='output.json', append=False):
        if not collection and in_notebook():
            collection = input('Please state collections name: ')
        if not collection:
            raise ValueError('You need to input a non-empty collection name!')

        if in_notebook() and not infile:
            from google.colab import files
            print('Upload your xlsx SEDL file:')
            uploaded = files.upload()
            for file_name in uploaded:
                infile = 'uploaded.xlsx'
                with open(infile, '+wb') as f:
                    f.write(uploaded[file_name])
                break
        
        if not infile:
            raise ValueError('You need to state an input file')

        unflattened, source_map = xl_to_json(infile, outfile)
        deal_indexes = set()
        org_indexes = set()

        for path, value in source_map.items():
            split_path = path.split('/')
            if len(split_path) < 2:
                continue
            index = int(split_path[1])
            for source_item in value:
                if source_item[0].lower().strip().startswith('deal'):
                    deal_indexes.add(index)
                if source_item[0].lower().strip().startswith('org'):
                    org_indexes.add(index)

        metadata = {key: value for key, value in unflattened.items() if key != 'deals'}

        deals = []
        orgs = []
        for num, obj in enumerate(unflattened['deals']):
            now = datetime.datetime.now()
            obj_id = obj.get('id')
            if num in deal_indexes:
                if not obj_id:
                    print('WARNING: object {} has no id field'.format(obj))
                    continue
                obj_id = obj.get('id')
                deals.append(dict(date_loaded=now, collection=collection, deal=obj, deal_id=obj_id, metadata=metadata))
            if num in org_indexes:
                if not obj_id:
                    obj['id'] = str(num)
                    print('WARNING: object {} has no id field'.format(obj))
                obj_id = obj.get('id')
                orgs.append(dict(date_loaded=now, collection=collection, organization=obj, org_id=obj_id, metadata=metadata))

        
        with self.db.engine.begin() as connection:
            if not append:
                connection.execute(''' delete from deal where collection = %s ''', collection)
                connection.execute(''' delete from organization where collection = %s ''', collection)

            if deals:
                insert = self.db.deal_table.insert()
                connection.execute(insert, deals)
            if orgs:
                insert = self.db.org_table.insert()
                connection.execute(insert, orgs)

        now = datetime.datetime.now()
        self.refresh_views()
        print("Loaded %s at: %s" % (collection, now))


    def refresh_views(self):
        with self.db.engine.begin() as connection:
            connection.execute('''REFRESH MATERIALIZED VIEW deal_summary; REFRESH MATERIALIZED VIEW collection_summary;''')


    def load_google_sheet(self, sheet_url=None, collection=None):
        if not in_notebook:
            raise Exception("Con not use google spreadsheets outside colab notebooks")

        xlsx_workbook = Workbook(write_only=True)
        gc = self.get_gspread_client()
        spreadsheet = gc.open_by_url(sheet_url)

        worksheets = spreadsheet.worksheets()

        for sheet in worksheets:
            if sheet.title.startswith('#'):
                continue
            xlsx_sheet = xlsx_workbook.create_sheet(sheet.title)
            data = spreadsheet.values_get(sheet.title, params={"valueRenderOption":"UNFORMATTED_VALUE", "dateTimeRenderOption": "FORMATTED_STRING"})
            values = data.get('values')
            if not values:
                continue
            data = fill_gaps(values)

            for row in data:
                xlsx_sheet.append(row)

        xlsx_workbook.save('converted.xlsx')
        self.load_xlsx(collection=collection, infile='converted.xlsx')


    def delete_collection(self, collection):
        with self.db.engine.begin() as connection:
            connection.execute('''delete from deal where collection = %s ''', collection)
            connection.execute('''delete from organization where collection = %s ''', collection)
        self.refresh_views()


    def get_results(self, sql, limit=-1, params=None, html=False, as_dicts=True):

        with self.db.engine.begin() as connection:
            params = params or []
            sql_result = connection.execute(sql, *params)
            if sql_result.returns_rows:
                results = {"headers": sql_result.keys()}
                if as_dicts:
                    data = []
                    for row in generate_rows(sql_result, limit, html):
                        data.append(OrderedDict(zip(sql_result.keys(), row)))
                    results["data"] = data
                else:
                    results["data"] = [row for row in generate_rows(sql_result, limit, html)]

                return results
            else:
                return "Success"


    def run_sql(self, sql, limit=100, params=None, display_full_json=False):
        from IPython.core.display import display, HTML
        results = self.get_results(sql, limit, params, html=True, as_dicts=False)
        if results == 'Success':
            return results
        results['display_full_json'] = display_full_json
        display(HTML(table.render(results)))


    def add_lookup_from_csv(self, lookup_name, key_name, infile=None):

        if in_notebook() and not infile:
            from google.colab import files
            print('Upload your csv file:')
            uploaded = files.upload()
            for file_name in uploaded:
                infile = 'uploaded.csv'
                with open(infile, '+wb') as f:
                    f.write(uploaded[file_name])
                break

        if not infile:
            raise ValueError('You need to state an input file')


        with self.db.engine.begin() as connection:
            connection.execute('''delete from lookup_table where lookup_name = %s''', lookup_name)
            rows = []
            with io.open(infile, "r", encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    rows.append(dict(lookup_name=lookup_name, data=row, lookup_key=row.get(key_name)))

            insert = self.db.lookup_table.insert()
            insert.execute(rows)

    def add_to_dashboard(self, collection):
        with self.db.engine.begin() as connection:
            connection.execute('''delete from dashboard where collection = %s ''', collection)
            connection.execute('''insert into dashboard values (%s) ''', collection)

    def delete_from_dashboard(self, collection):
        with self.db.engine.begin() as connection:
            connection.execute('''delete from dashboard where collection = %s ''', collection)
