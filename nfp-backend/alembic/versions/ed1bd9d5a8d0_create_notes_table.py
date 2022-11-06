"""create notes table

Revision ID: ed1bd9d5a8d0
Revises: 
Create Date: 2022-11-05 16:03:52.733211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed1bd9d5a8d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "notes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.String),
        sa.Column("completed", sa.Boolean)
    )


def downgrade():
    op.drop_table("notes")
