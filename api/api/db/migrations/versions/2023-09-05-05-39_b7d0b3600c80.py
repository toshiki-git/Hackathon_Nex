"""Add game_tag table

Revision ID: b7d0b3600c80
Revises: bf6a733cd5ae
Create Date: 2023-09-05 05:39:08.862868

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "b7d0b3600c80"
down_revision = "bf6a733cd5ae"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "game_tag",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_game_tag_title"), "game_tag", ["title"], unique=False)
    op.create_table(
        "timeline_post_tag_association",
        sa.Column("timeline_post_id", sa.Integer(), nullable=False),
        sa.Column("game_tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["game_tag_id"],
            ["game_tag.id"],
        ),
        sa.ForeignKeyConstraint(
            ["timeline_post_id"],
            ["timeline_posts.post_id"],
        ),
        sa.PrimaryKeyConstraint("timeline_post_id", "game_tag_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("timeline_post_tag_association")
    op.drop_index(op.f("ix_game_tag_title"), table_name="game_tag")
    op.drop_table("game_tag")
    # ### end Alembic commands ###
