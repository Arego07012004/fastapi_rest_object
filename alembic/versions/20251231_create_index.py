from alembic import op
import sqlalchemy as sa

revision = '20251231_create_index'
down_revision = '20251231_add_rating'
branch_labels = None
depends_on = None

def upgrade():
    op.create_index('ix_students_name', 'students', ['name'])

def downgrade():
    op.drop_index('ix_students_name', table_name='students')
