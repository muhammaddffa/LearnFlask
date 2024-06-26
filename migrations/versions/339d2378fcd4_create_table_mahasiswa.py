"""create table mahasiswa

Revision ID: 339d2378fcd4
Revises: 1cf608d68bff
Create Date: 2024-01-29 17:04:39.652573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '339d2378fcd4'
down_revision = '1cf608d68bff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mahasiswa',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nim', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('dosen_satu', sa.BigInteger(), nullable=True),
    sa.Column('dosen_dua', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['dosen_dua'], ['dosen.id'], ),
    sa.ForeignKeyConstraint(['dosen_satu'], ['dosen.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mahasiswa')
    # ### end Alembic commands ###
