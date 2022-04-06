from psycopg2 import pool
from psycopg2.extras import RealDictCursor
import logging

try: 
    connection_pool = pool.SimpleConnectionPool(1, 5, host="dbservice", port=5432,
                                                database="test",
                                                user="postgres",
                                                password="Testing123")
except Exception as e:
    connection_pool = None
    logging.info(str(e))


"""
Queries 
"SELECT * from counties limit 10;"

"SELECT * from counties WHERE id = {id}
"""

def get_top_10():
    if connection_pool != None:
        conn = connection_pool.getconn()
        values = None
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * from counties limit 10;")
            values = cursor.fetchall()
        connection_pool.putconn(conn)
        return values
    return {"error":"conneting to db"}

def get_one_country(id_):
    if connection_pool != None:
        conn = connection_pool.getconn()
        values = None
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            values = cursor.execute(f"SELECT * from counties WHERE id = {id_}")
            values = cursor.fetchall()
        connection_pool.putconn(conn)
        return values
    return {"error":"conneting to db"}