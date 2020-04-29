import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table_query_1='CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username text,password text)'

cursor.execute(create_table_query_1)

create_table_query_2='CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY,name text,price real)'
cursor.execute(create_table_query_2)

connection.commit()
connection.close()