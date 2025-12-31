from alembic import op
import sqlalchemy as sa

revision = '20251231_add_rating'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('movies', sa.Column('rating', sa.Float(), nullable=True))

def downgrade():
    op.drop_column('movies', 'rating')
