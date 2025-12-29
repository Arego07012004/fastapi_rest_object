import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_NAME = "harward_university"
DB_USER = "areg"
DB_PASSWORD = "7125"
DB_HOST = "localhost"
DB_PORT = 5423

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

print("Successfully connected to the database!")

#Check if role exists
cur.execute(f"SELECT 1 FROM pg_roles WHERE rolname='{DB_USER}';")
if not cur.fetchone():
    cur.execute(f"CREATE ROLE {DB_USER} LOGIN PASSWORD '{DB_PASSWORD}';")
    print(f"Role {DB_USER} created")
else:
    print(f"Role {DB_USER} already exists")

#Check if database exists
cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{DB_NAME}';")
if not cur.fetchone():
    cur.execute(f"CREATE DATABASE {DB_NAME} OWNER '{DB_USER}';")
    print(f"Database {DB_NAME} created")
else:
    print(f"Database {DB_NAME} already exists")

cur.close()
conn.close()
print("Database and user created successfully!")
