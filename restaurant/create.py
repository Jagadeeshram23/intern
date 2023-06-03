import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

# conn.execute('DROP TABLE restaurant;')
conn.execute('CREATE TABLE restaurant(table_no numeric(2) primary key, customer varchar(30) not null,ph_no numeric(12) not null,email varchar(50),count numeric(2) not null,date date not null,time_slot time not null);')
print("Created table successfully!")

conn.close()