"""create picks table

Revision ID: 307948a2e966
Revises: 21f674e3839f
Create Date: 2021-03-30 15:13:44.282943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '307948a2e966'
down_revision = '21f674e3839f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('picks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('year', sa.String(length=4)),
    sa.Column('editorial', sa.Text(), nullable=True),
    sa.Column('original_poster', sa.String(length=500)),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('media_id', sa.Integer(), nullable=False),
    sa.Column('imdb_id', sa.String(length=50), nullable=True),
    sa.Column('list_id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['lists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('picks')
    # ### end Alembic commands ###
