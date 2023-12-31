"""Edit users table

Revision ID: 92298a2aa9fe
Revises: bf6a733cd5ae
Create Date: 2023-09-06 13:04:23.614373

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "92298a2aa9fe"
down_revision = "bf6a733cd5ae"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("display_name", sa.String(length=50), nullable=False)
    )
    op.add_column("users", sa.Column("is_initialized", sa.Boolean(), nullable=False))
    op.alter_column(
        "users", "username", existing_type=sa.VARCHAR(length=50), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users", "username", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.drop_column("users", "is_initialized")
    op.drop_column("users", "display_name")
    # ### end Alembic commands ###
