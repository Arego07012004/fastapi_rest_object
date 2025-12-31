import sys
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from app.database import Base, SQLALCHEMY_DATABASE_URL
from app.models import Student

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

print("Creating table students...")
try:
    Base.metadata.create_all(bind=engine, tables=[Student.__table__], checkfirst=True)
    print("Table students created successfully")
except Exception as e:
    print(f"Failed to create table students: {e}")
    sys.exit(1)

