import psycopg2
import logging

#connection to PostgreSQL

connection=psycopg2.connect(
    database="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432")

print(connection)


delete_sql_query="""
            DELETE FROM customer WHERE id=4
"""

pointer=connection.cursor()

pointer.execute(delete_sql_query)
connection.commit()
print("record is deleted")
connection.close()