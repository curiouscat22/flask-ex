from psycopg2 import pool
from psycopg2.extras import RealDictCursor
import logging

# -----
import psycopg2
from sqlalchemy import create_engine
import csv


engine = create_engine('postgresql+psycopg2://postgres:Testing123@dbservice:5432/postgres')
conn = engine.connect()
try:
    conn.execute("CREATE database IF NOT EXISTS test1")
    conn.execute("commit")
except Exception as e:
    print(e)
finally:
    conn.close()

# copy csv to postgres
conn = psycopg2.connect(database="test", user="postgres", password="Testing123", host="dbservice", port="5432")
cursor = conn.cursor()

# create table
cursor.execute("CREATE TABLE IF NOT EXISTS countries (id serial PRIMARY KEY, country varchar(200), alpha2 char(30), alpha3 char(30), nuCode int, latitude float, longitude float)")
# copy data from csv to table
with open('countries.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("INSERT INTO countries (country, alpha2, alpha3, nuCode, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s)", (row['Country'], row['Alpha2_code'], row['Alpha3_code'], row['Numeric_code'], row['Latitude'], row['Longitude']))
conn.commit()
conn.close()
# ---

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
"SELECT * from countries limit 10;"

"SELECT * from countries WHERE id = {id}
"""

def get_top_10():
    if connection_pool != None:
        conn = connection_pool.getconn()
        values = None
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * from countries limit 10;")
            values = cursor.fetchall()
        connection_pool.putconn(conn)
        return values
    return {"error":"conneting to db"}

def get_one_country(id_):
    if connection_pool != None:
        conn = connection_pool.getconn()
        values = None
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            values = cursor.execute(f"SELECT * from countries WHERE id = {id_}")
            values = cursor.fetchall()
        connection_pool.putconn(conn)
        return values
    return {"error":"conneting to db"}