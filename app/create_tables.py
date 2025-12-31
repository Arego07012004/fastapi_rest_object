import sys
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from app.database import Base, SQLALCHEMY_DATABASE_URL
from app.models import Student, Faculty, Course

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"connect_timeout": 5}
)

try:
    with engine.connect() as conn:
        print("Connected to PostgreSQL successfully")
except OperationalError as e:
    print("Cannot connect to PostgreSQL:", e)
    sys.exit(1)

tables = [Faculty.__table__, Course.__table__, Student.__table__]

for table in tables:
    print(f"Creating table {table.name}...")
    try:
        Base.metadata.create_all(bind=engine, tables=[table], checkfirst=True)
        print(f"Table {table.name} created successfully")
    except Exception as e:
        print(f"Failed to create table {table.name}: {e}")
        sys.exit(1)

print("All tables created successfully!")

