import psycopg2
from sqlalchemy import create_engine
import csv


engine = create_engine('postgresql+psycopg2://postgres:Testing123@dbservice:5432/postgres')
conn = engine.connect()
conn.execute("commit")
conn.execute("create database test")
conn.execute("commit")
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