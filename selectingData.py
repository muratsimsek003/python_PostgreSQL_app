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


table_select_query="""
            SELECT * FROM customer
"""


pointer=connection.cursor()

results=pointer.execute(table_select_query)
rows=pointer.fetchall()
for row in rows:
    print(row)

for row in rows:
    print(row[1],"-----Loan Amount--------",row[-1])


file=open("data.txt","w")
for row in rows:
    file.writelines(row[1])