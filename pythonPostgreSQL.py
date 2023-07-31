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

connection.autocommit=True

table_customer_query="""
            CREATE TABLE customer(
            ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL, 
            AGE INT NOT NULL,
            ADDRESS CHAR(100),
            LOAN_AMOUNT REAL)
"""


pointer=connection.cursor()

try:
    pointer.execute(table_customer_query)
    connection.commit()
    logging.info("Table is created")

except Exception as e:
    logging.error("Table is dublicated ", e)

finally:
    connection.close()















