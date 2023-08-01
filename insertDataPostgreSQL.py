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


insert_sql_query="""

    INSERT INTO customer(ID, NAME, AGE, ADDRESS, LOAN_AMOUNT)
    VALUES(2, 'Murat', 37, 'NY', 2000.45)
"""

pointer=connection.cursor()

pointer.execute(insert_sql_query)
connection.commit()
print("record is created")
connection.close()