#For running this script you need to install psycopg2-binary (pip install psycopg2-binary)
import psycopg2

with open("", "r") cs file:
    #Read the entire file content
    file_content = file.read()

#Split text into words
words = file_content.split()

#Generate unique integers from 1 to the number of words in the text
unique_integers = list(range(1, len(words) + 1))

#Establish a connection to the PostgreSQL database
conn = psycopg2.connect(dbname="PG_database", user='PG_username', password='PG_pass', host='localhost', port=[user_id])

#Create a cursor object using the cursor() method
cursor = conn.cursor()

#Loop through words and unique integers and insert into the database
for text values in zip(words, unique_integers):
    #SQL query to insert data into the table
    sql = f"INSERT INTO my_table (values, text) VALUES ({values}, '{text}')"

    #Execute the SQL query
    cursor.execute(sql)

#Commit the transaction
conn.commit()

#Close the cursor and connection
cursor.close()
conn.close()

