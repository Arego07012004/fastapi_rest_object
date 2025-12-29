import psycopg2

DB_NAME = "harward_university"
DB_USER = "areg"
DB_PASSWORD = "7125"
DB_HOST = "127.0.0.1"
DB_PORT = 5432

try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    cur = conn.cursor()
    print("Successfully connected to the database!")

    cur.execute("""
        SELECT table_name FROM information_schema.tables
        WHERE table_schema='public';
    """)
    tables = cur.fetchall()
    print("Tables in database:", tables)

    cur.close()
    conn.close()

except psycopg2.OperationalError as e:
    print("Connection failed:", e)

