import psycopg2, sys
if sys.platform != "win32":
    path = "/opt/flask_app/"
    sys.path.append(path)
    path += "api"
else:
    path = ".."
from db_interact.db_connection import db_connection


def get_api_key():
    try:
        connection_db = db_connection()
        connection_db.autocommit = True
        cursor = connection_db.cursor()
        cursor.execute("SELECT apikey from apikey")
        key = cursor.fetchall()
        return key[0][0]
    except (Exception, psycopg2.Error) as error:
        print("Error get api key from PostGreSQL table")
        print("Error displayed : " + str(error))