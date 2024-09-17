"""Renaming students to scholars

Revision ID: 87ae4431b708
Revises: 
Create Date: 2024-09-14 19:47:53.109921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87ae4431b708'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    
