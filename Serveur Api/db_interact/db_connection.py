import psycopg2


def db_connection():
    return psycopg2.connect(database="api", host="90.120.40.224", user="apiuser", password="apiuser")
