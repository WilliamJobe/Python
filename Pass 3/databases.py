import sqlite3

conn = sqlite3.connect('test.db')
print("Databas öppnad!")

#create table
#conn.execute('''CREATE TABLE test (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL,AGE INT NOT NULL);''')
#print("Tabell skapad!")

#insert data
#conn.execute("INSERT INTO test (ID,NAME,AGE) VALUES (1, 'Elvis', 99)")
#conn.execute("INSERT INTO test (ID,NAME,AGE) VALUES (2, 'Stephen Hawking', 76)")
#conn.execute("INSERT INTO test (ID,NAME,AGE) VALUES (3, 'Shaq', 50)")
#conn.commit()

#read data
cursor = conn.execute("SELECT id, name, age from test")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("AGE = ", str(row[2]), "\n")

conn.close()