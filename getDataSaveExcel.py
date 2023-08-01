import psycopg2
from openpyxl import Workbook


def get_postgresql_connection():

    connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432")

    return connection


def fetch_data_from_table(connection, table_name):
    # Veritabanından tablodaki tüm verileri çekme
    query = f"SELECT * FROM {table_name};"
    pointer = connection.cursor()
    pointer.execute(query)
    data = pointer.fetchall()
    pointer.close()
    return data


def save_to_excel(data, output_file):
    # Verileri Excel dosyasına kaydetme
    wb = Workbook()
    ws = wb.active

    # Verileri Excel tablosuna yazma
    for row in data:
        ws.append(row)

    # Excel dosyasını kaydetme
    wb.save(output_file)


def main():
    try:
        # PostgreSQL veritabanına bağlantı oluşturma
        connection = get_postgresql_connection()

        # Tablodaki verileri çekme
        table_name = "customer"
        data = fetch_data_from_table(connection, table_name)

        # Verileri Excel dosyasına kaydetme
        output_file = "output.xlsx"
        save_to_excel(data, output_file)

        print(f"Excel file is saved.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Bağlantıyı kapatma
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    main()
