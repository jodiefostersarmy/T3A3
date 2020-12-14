"""renamed account model to user

Revision ID: 1a19e58e8203
Revises: 
Create Date: 2020-11-21 08:41:28.509853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a19e58e8203'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leagues',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('leagues_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='leagues_pkey'),
    sa.UniqueConstraint('title', name='leagues_title_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('accounts',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('accounts_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='accounts_pkey'),
    sa.UniqueConstraint('email', name='accounts_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('account_leagues',
    sa.Column('account_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('league_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], name='account_leagues_account_id_fkey'),
    sa.ForeignKeyConstraint(['league_id'], ['leagues.id'], name='account_leagues_league_id_fkey')
    )
    op.drop_table('profiles')
    op.drop_table('users')
    # ### end Alembic commands ###
