import sys

if sys.platform != "win32":
    path = "/opt/flask_app/"
    sys.path.append(path)
    path += "api"
else:
    path = ".."
from db_interact.check_film_already_exist import check_film_already_exist
from db_interact.db_connection import db_connection

def insert_list_item(data, type):

    connection_db = db_connection()
    connection_db.autocommit = True
    cursor = connection_db.cursor()
    if check_film_already_exist(data[0], type):
        query = f"INSERT INTO {type} VALUES ('{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}', {data[0]}, '{data[7]}');"
        try:
            cursor.execute(query)
        except Exception as e:
            print("Error when insert new "+ type +" in the database. Error : " + str(e))

