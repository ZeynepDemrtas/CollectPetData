import mysql.connector
import json
import os

def connect_database():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password") 

def read_file(file_name):
    with open(file_name, 'r') as file:
        file_data = file.read()
    return file_data

if __name__ == '__main__':
    with open(os.path.abspath(os.getcwd()) + '\petlebi_products.json', encoding="utf-8") as json_file:
        product_data = json.load(json_file)

    create_table_command = read_file(os.path.abspath(os.getcwd()) + '\petlebi_create.sql')
    inserting_data_command = read_file(os.path.abspath(os.getcwd()) + '\petlebi_insert.sql')

    mydb = connect_database()
    cursor_create = mydb.cursor()
    cursor_create.execute(create_table_command)
    cursor_create.close()

    mydb = connect_database()
    cursor_insert = mydb.cursor()
    for data in product_data:
        cursor_insert.execute(inserting_data_command,
                        (data['product URL'], data['product name'], data['product barcode'],
                        float(data['product price']), data['product stock'], data['product images'],
                        data['description'], data['sku'], data['category'], int(data['product_id']), data['brand']))

    mydb.commit()
    cursor_insert.close()
    mydb.close()


