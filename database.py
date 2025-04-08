import sqlite3 as sl

conn =sl.connect('test.db')

print ('Connected to test.db') 

conn.execute('''
    CREATE TABLE IF NOT EXIST USER(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER 
            );
''')
sql = 'INSERT INTO USER(id, name, age) Values(?,?,?)'

data = [
    (1, 'Alice', 21),
    (2, 'Bob', 22),
    (3, 'Paula', 30)
]
with conn:
    conn.executemany(sql,data)

data = conn.execute ('SELECT *FROM USER WHERE age>=22')

for row in data:
  print(row)