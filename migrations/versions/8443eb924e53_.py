"""empty message

Revision ID: 8443eb924e53
Revises: 57418f3802c6
Create Date: 2020-05-28 11:00:47.198349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8443eb924e53'
down_revision = '57418f3802c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empEngs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('q14_howMany', sa.String(length=10), nullable=True),
    sa.Column('q13_pleaseRate_0', sa.String(length=10), nullable=True),
    sa.Column('q13_pleaseRate_1', sa.String(length=10), nullable=True),
    sa.Column('q13_pleaseRate_2', sa.String(length=10), nullable=True),
    sa.Column('q13_pleaseRate_3', sa.String(length=10), nullable=True),
    sa.Column('q13_pleaseRate_4', sa.String(length=10), nullable=True),
    sa.Column('q13_pleaseRate_5', sa.String(length=10), nullable=True),
    sa.Column('q13_pleaseRate_6', sa.String(length=10), nullable=True),
    sa.Column('q3_howWould3_0', sa.String(length=10), nullable=True),
    sa.Column('q3_howWould3_1', sa.String(length=10), nullable=True),
    sa.Column('q3_howWould3_2', sa.String(length=10), nullable=True),
    sa.Column('q3_howWould3_3', sa.String(length=10), nullable=True),
    sa.Column('q3_howWould3_4', sa.String(length=10), nullable=True),
    sa.Column('q4_typeA4_0', sa.String(length=10), nullable=True),
    sa.Column('q4_typeA4_1', sa.String(length=10), nullable=True),
    sa.Column('q4_typeA4_2', sa.String(length=10), nullable=True),
    sa.Column('q4_typeA4_3', sa.String(length=10), nullable=True),
    sa.Column('q5_howWould_0', sa.String(length=10), nullable=True),
    sa.Column('q5_howWould_1', sa.String(length=10), nullable=True),
    sa.Column('q5_howWould_2', sa.String(length=10), nullable=True),
    sa.Column('q5_howWould_3', sa.String(length=10), nullable=True),
    sa.Column('q5_howWould_4', sa.String(length=10), nullable=True),
    sa.Column('q6_howWould6_0', sa.String(length=10), nullable=True),
    sa.Column('q6_howWould6_1', sa.String(length=10), nullable=True),
    sa.Column('q6_howWould6_2', sa.String(length=10), nullable=True),
    sa.Column('q6_howWould6_3', sa.String(length=10), nullable=True),
    sa.Column('q6_howWould6_4', sa.String(length=10), nullable=True),
    sa.Column('q10_anyComments10', sa.String(length=4096), nullable=True),
    sa.Column('q7_name_first', sa.String(length=25), nullable=True),
    sa.Column('q7_name_last', sa.String(length=25), nullable=True),
    sa.Column('q8_email', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('empEngs')
    # ### end Alembic commands ###
