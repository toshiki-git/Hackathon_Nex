"""Add hashtag

Revision ID: 4124e28836d1
Revises: 6eee6587a1dc
Create Date: 2023-09-06 08:32:47.508299

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "4124e28836d1"
down_revision = "6eee6587a1dc"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "hash_tag",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("hashtag", sa.String(length=100), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("game_tag")
    op.add_column(
        "timeline_post",
        sa.Column("hashtags", postgresql.ARRAY(sa.String(length=100)), nullable=True),
    )
    op.drop_column("timeline_post", "game_ids")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "timeline_post",
        sa.Column(
            "game_ids",
            postgresql.ARRAY(sa.INTEGER()),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_column("timeline_post", "hashtags")
    op.create_table(
        "game_tag",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("title", sa.VARCHAR(length=100), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="game_tag_pkey"),
    )
    op.drop_table("hash_tag")
    # ### end Alembic commands ###
