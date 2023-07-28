import psycopg2

#PostgreSQL 14'e sağ tıklayıp açılan menüden "properties" tıkla.
#Properties de bulunan Connection seçeneğini tıkla.
#burada bulunan Host name/address, Port, ve Maintenance database  ve Username bilgilerini kullan.
#database_name e Maintenance database i yaz.
#user_name e Username de bulunan bilgiyi yaz.

database_name="postgres"
user_name="postgres"
password="1234"
host_ip="localhost"
host_port="5432"


baglanti=psycopg2.connect(database=database_name,
                          user=user_name,
                          password=password,
                          host=host_ip,
                          port=host_port)



baglanti.autocommit=True   #veritabanına execute etme yetkisi vermek içn kullanılır


cursor=baglanti.cursor()   #satır olarak yazdığımız SQL kodları kabul eder


query="CREATE DATABASE pythonapp_db"   #pythonAPP_db adında bir database oluştur

cursor.execute(query)          #yukarıdaki query i çalıştır

#şimdi bu oluşturuduğumuz database e bağlanalim


database_name="pythonapp_db"

baglanti=psycopg2.connect(database=database_name,
                          user=user_name,
                          password=password,
                          host=host_ip,
                          port=host_port)


#oluşturuduğumuz database e bir tablo oluşturalım

query_create_table= """                    
CREATE TABLE IF NOT EXISTS cars(
id SERIAL PRIMARY KEY,
name TEXT NOT NULL,
model INTEGER,
number TEXT,
colour TEXT,
company TEXT)
"""
baglanti.autocommit=True   #veritabanına execute etme yetkisi vermek içn kullanılır
cursor.execute(query_create_table)

#INSERT işlemleri

cars=[
("Aqua", 20999, "ABC123", "Red", "Toyato"),
( "700s ",2015, "Vezel", "Black" ,"BMW")
]

car_record=", ".join(["%s"]*len(cars))
query_insert=(f"INSERT INTO cars (name, model, number, colour,company)"
              f"VALUES{car_record}")

baglanti.autocommit=True
cursor.execute(query_insert, cars)


#READ- SELECT

query_select= "SELECT * FROM cars"
baglanti.autocommit=True
cursor.execute(query_select)
cars=cursor.fetchall()
for car in cars:
    print(car)

# UPDATE

query_update="""
UPDATE cars
SET colour = "Black"
WHERE model >=2010
"""
cursor.execute(query_update)

