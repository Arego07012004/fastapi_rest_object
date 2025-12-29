import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_NAME = "harward_university"
DB_USER = "areg"
DB_PASSWORD = "7125"
DB_HOST = "localhost"
DB_PORT = 5432

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres"
    host=DB_HOST
    port=DB_PORT
)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

# User
cur.execute(f"""
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = '{DB_USER}') THEN
       CREATE ROLE {DB_USER} LOGIN PASSWORD '{DB_PASSWORD}';
    END IF;
END
$$;
""")

# Base
cur.execute(f"""
SELECT 'CREATE DATABASE {DB_NAME} OWNER {DB_USER}'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '{DB_NAME}');
""")

conn.close()
print("Database initialized")
