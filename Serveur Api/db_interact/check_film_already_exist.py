import psycopg2, sys

if sys.platform != "win32":
    path = "/opt/flask_app/"
    sys.path.append(path)
    path += "api"
else:
    path = ".."
from db_interact.db_connection import db_connection


def check_film_already_exist(id_movie, type):
    try:
        connection_db = db_connection()
        connection_db.autocommit = True
        cursor = connection_db.cursor()
        cursor.execute(f"SELECT * from {type} where id_movie = {id_movie}")
        key = cursor.fetchall()
        if len(key)>0:
            return 0
        else:
            return 1
    except (Exception, psycopg2.Error) as error:
        print("Error get api key from PostGreSQL table")

        print("Error displayed : " + str(error))
