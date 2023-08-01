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

update_sql_query="""

    UPDATE customer SET AGE=65 WHERE ID=4
"""

pointer=connection.cursor()

try:
    pointer.execute(update_sql_query)
    connection.commit()
    logging.info("Table is created")
    print("record is updated")

except Exception as e:
    logging.error("Error ", e)

finally:
    connection.close()