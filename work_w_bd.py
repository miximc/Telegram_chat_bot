import sqlite3

comm = sqlite3.connect('bd_bot2.sqlite3')

cursor = comm.cursor()

#cursor.execute('DROP TABLE completed_tasks')
cursor.execute('''CREATE TABLE IF NOT EXISTS completed_tasks(
    id INTEGER,
    name VARCHAR(50), PRIMARY KEY (id))''')

# cursor.execute('DROP TABLE unfifshed_tasks')
# cursor.execute('''CREATE TABLE unfifshed_tasks(
#     id INTEGER,
#     name VARCHAR(50), PRIMARY KEY (id))''')
a = 'work'
request = f'INSERT INTO completed_tasks(name) VALUES ("{a}")'

cursor.execute(request)

vals = cursor.execute('SELECT * FROM completed_tasks')
for v in vals:
    print(type(str(v)))