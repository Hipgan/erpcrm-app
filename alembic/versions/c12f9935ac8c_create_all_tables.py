"""create all tables

Revision ID: c12f9935ac8c
Revises: 
Create Date: 2025-06-01 19:17:44.606122

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c12f9935ac8c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contracts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('total_amount', sa.Float(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('number_of_installments', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contracts_id'), 'contracts', ['id'], unique=False)
    op.create_table('purchases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('purchase_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_purchases_id'), 'purchases', ['id'], unique=False)
    op.drop_index(op.f('ix_Products_id'), table_name='Products')
    op.drop_index(op.f('ix_Products_name'), table_name='Products')
    op.drop_table('Products')
    op.add_column('payments', sa.Column('contract_id', sa.Integer(), nullable=False))
    op.drop_constraint(op.f('payments_customer_id_fkey'), 'payments', type_='foreignkey')
    op.create_foreign_key(None, 'payments', 'contracts', ['contract_id'], ['id'])
    op.drop_column('payments', 'customer_id')
    op.add_column('products', sa.Column('price', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'price')
    op.add_column('payments', sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'payments', type_='foreignkey')
    op.create_foreign_key(op.f('payments_customer_id_fkey'), 'payments', 'customers', ['customer_id'], ['id'])
    op.drop_column('payments', 'contract_id')
    op.create_table('Products',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('Products_pkey'))
    )
    op.create_index(op.f('ix_Products_name'), 'Products', ['name'], unique=True)
    op.create_index(op.f('ix_Products_id'), 'Products', ['id'], unique=False)
    op.drop_index(op.f('ix_purchases_id'), table_name='purchases')
    op.drop_table('purchases')
    op.drop_index(op.f('ix_contracts_id'), table_name='contracts')
    op.drop_table('contracts')
    # ### end Alembic commands ###
