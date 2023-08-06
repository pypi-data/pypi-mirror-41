"""create materialized views

Revision ID: 3d8b428eb9d3
Revises: f0771214ae1e
Create Date: 2019-01-22 10:52:50.589667

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3d8b428eb9d3'
down_revision = 'f0771214ae1e'
branch_labels = None
depends_on = None


def upgrade():
    create_view_statements = '''
    drop view collection_summary;
    drop view deal_summary;

    create MATERIALIZED view deal_summary
    as
    select 
       id deal_table_id,
       deal_id,
       collection,
       deal->'recipientOrganization'->>'name' as recipient_organization_name,
       deal->'recipientOrganization'->>'id' as recipient_organization_id,
       deal->'arrangingOrganization'->>'name' as arraging_organization_name,
       deal->'arrangingOrganization'->>'id' as arraging_organization_id,
       deal->>'status' as status,
       deal->>'currency' currency,
       coalesce(convert_to_numeric(deal->>'estimatedValue')::numeric, 0) as estimated_value,
       coalesce(convert_to_numeric(deal->>'value')::numeric, 0) as value,
       coalesce(offer_count, 0) as offer_count,
       coalesce(csu_standard_mark_awarded, 0) as csu_standard_mark_awarded,
       coalesce(investment_target, 0) as investment_target,
       coalesce(minimum_investment_target, 0) as minimum_investment_target,
       coalesce(maximum_investment_target, 0) as maximum_investment_target,
       coalesce(project_estimated_value, 0) as project_estimated_value,
       coalesce(project_raised_value, 0) as project_raised_value,
       coalesce(project_count, 0) as project_count,
       coalesce(asset_purchase_price, 0) as asset_purchase_price,
       coalesce(asset_quantity, 0) as asset_quantity,
       coalesce(asset_count, 0) as asset_count,
       coalesce(asset_value, 0) as asset_value,
       coalesce(grant_count, 0) as grant_count,
       coalesce(is_match_funding, 0) as is_match_funding,
       coalesce(grant_amount_committed, 0) as grant_amount_committed,
       coalesce(grant_amount_disbursed, 0) as grant_amount_disbursed,
       coalesce(grant_amount_requested, 0) as grant_amount_requested,
       coalesce(equity_count, 0) as equity_count,
       coalesce(equity_value, 0) as equity_value,
       coalesce(equity_estimated_value, 0) as equity_estimated_value,
       coalesce(credit_count, 0) as credit_count,
       coalesce(credit_estimated_value, 0) as credit_estimated_value,
       coalesce(credit_value, 0) as credit_value,
       deal
    from deal
       left join offer_summary os on os.deal_table_id = deal.id
       left join project_summary ps on ps.deal_table_id = deal.id
       left join grant_summary gs on gs.deal_table_id = deal.id
       left join equity_summary es on es.deal_table_id = deal.id
       left join credit_summary cs on cs.deal_table_id = deal.id;


    create MATERIALIZED view collection_summary
    as
    select 
       collection,
       count(*) deal_count,
       sum(estimated_value) as estimated_value,
       sum(value) as value,
       sum(offer_count) as offer_count,
       sum(csu_standard_mark_awarded) as csu_standard_mark_awarded,
       sum(investment_target) as investment_target,
       sum(minimum_investment_target) as minimum_investment_target,
       sum(maximum_investment_target) as maximum_investment_target,
       sum(project_estimated_value) as project_estimated_value,
       sum(project_raised_value) as project_raised_value,
       sum(project_count) as project_count,
       sum(asset_purchase_price) as asset_purchase_price,
       sum(asset_quantity) as asset_quantity,
       sum(asset_count) as asset_count,
       sum(asset_value) as asset_value,
       sum(grant_count) as grant_count,
       sum(is_match_funding) as is_match_funding,
       sum(grant_amount_committed) as grant_amount_committed,
       sum(grant_amount_disbursed) as grant_amount_disbursed,
       sum(grant_amount_requested) as grant_amount_requested,
       sum(equity_count) as equity_count,
       sum(equity_value) as equity_value,
       sum(equity_estimated_value) as equity_estimated_value,
       sum(credit_count) as credit_count,
       sum(credit_estimated_value) as  credit_estimated_value,
       sum(credit_value) as credit_value
    from deal_summary
    group by 1;
    '''

    op.execute(create_view_statements)

def downgrade():
    pass
