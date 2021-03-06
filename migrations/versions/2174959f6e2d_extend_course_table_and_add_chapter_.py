"""extend course table and add chapter table

Revision ID: 2174959f6e2d
Revises: 27aa6a57d787
Create Date: 2018-03-14 16:38:27.488388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2174959f6e2d'
down_revision = '27aa6a57d787'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chapter',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('vedio_url', sa.String(length=256), nullable=True),
    sa.Column('vedio_duration', sa.String(length=24), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chapter_name'), 'chapter', ['name'], unique=True)
    op.add_column('course', sa.Column('description', sa.String(length=256), nullable=True))
    op.add_column('course', sa.Column('image_url', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'image_url')
    op.drop_column('course', 'description')
    op.drop_index(op.f('ix_chapter_name'), table_name='chapter')
    op.drop_table('chapter')
    # ### end Alembic commands ###
