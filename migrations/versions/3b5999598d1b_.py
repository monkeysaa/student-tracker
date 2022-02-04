"""empty message

Revision ID: 3b5999598d1b
Revises: 
Create Date: 2022-02-03 18:03:08.228554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b5999598d1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('affixes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('affix', sa.String(), nullable=False),
    sa.Column('location', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('consonants',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('chars', sa.String(length=3), nullable=False),
    sa.Column('complex_c', sa.Boolean(), nullable=False),
    sa.Column('location', sa.Integer(), nullable=True),
    sa.Column('blend', sa.Boolean(), nullable=False),
    sa.Column('blocker', sa.Boolean(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('v_level', sa.Integer(), nullable=True),
    sa.Column('c_level', sa.Integer(), nullable=True),
    sa.Column('a_level', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vowels',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('chars', sa.String(length=5), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('origin', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_affixes',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('affix_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['affix_id'], ['affixes.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'affix_id')
    )
    op.create_table('student_consonants',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('cons_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cons_id'], ['consonants.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'cons_id')
    )
    op.create_table('student_vowels',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('vowel_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.ForeignKeyConstraint(['vowel_id'], ['vowels.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'vowel_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_vowels')
    op.drop_table('student_consonants')
    op.drop_table('student_affixes')
    op.drop_table('vowels')
    op.drop_table('students')
    op.drop_table('consonants')
    op.drop_table('affixes')
    # ### end Alembic commands ###