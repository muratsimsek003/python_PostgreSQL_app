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

insert_sql_query="""

    INSERT INTO customer(ID, NAME, AGE, ADDRESS, LOAN_AMOUNT)
    VALUES(1, 'JOHN', 37, 'NY', 1000.45)
"""

pointer=connection.cursor()

pointer.execute(insert_sql_query)
pointer.commit()
print("record is created")
connection.close()