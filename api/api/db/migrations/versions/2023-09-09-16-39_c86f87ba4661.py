"""merge heads

Revision ID: c86f87ba4661
Revises: 92298a2aa9fe, 39698ded2f2e
Create Date: 2023-09-09 16:39:44.173275

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "c86f87ba4661"
down_revision = ("92298a2aa9fe", "39698ded2f2e")
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
