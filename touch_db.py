# ДЗ Для ТГ Бота: сохранять список дел в базе данных
# ДЗ Для почты: сохранять в базе данных статистику: когда получено письмо и от кого.
# Само письмо хранить не нужно. 


import sqlite3
# Библиотека для подключения к Базе Данных sqlite

#conn = sqlite3.connect(r'Z:\4. ГК\Python221\20230228_db\reg_user\db.sqlite3')
# Даём имя файла. Если его (файла) не было, он будет создан (при наличии прав)
#conn = sqlite3.connect('C:\\Windows\\kuku.sql3')  Ошибка прав доступа

conn = sqlite3.connect('bd_bot3.sqlite3')

# В других бд потребуется хост (ip или домен), пользователь и пароль

cursor = conn.cursor()

# Запросы к БД представляют собой с точки зрения питона текстовые строки


# SQL Case Insensitive

# CREATE DATABASE name - создать базу данных (MySql, Oracle, Postresql, MsSQl)

# CREATE TABLE flowers(id INT, name VARCHAR(4), price FLOAT, PRIMARY KEY (id));
#cursor.execute('''DROP TABLE flowers''')

cursor.execute('''CREATE TABLE IF NOT EXISTS flowers(
    id INTEGER PRIMARY KEY, name VARCHAR(4), price FLOAT)''')

# первичный ключ - уникальный (т.е. нет второй строки с таким же значением)
#                  непустой (нет null)

#        id      name    price
#


request = '''
INSERT INTO flowers(name, price)
 VALUES ('violet', 50)'''

cursor.execute(request)

request = '''
INSERT INTO flowers(name, price)
 VALUES ('iris', 70)'''

cursor.execute(request)

request = '''
INSERT INTO flowers(name, price)
 VALUES ('rose',  100)'''

cursor.execute(request)
conn.commit()
vals = cursor.execute('SELECT * FROM flowers')
for v in vals:
    print(v)

# В части WHERE сравнение на равенство делается ОДНИМ знаком равно
#                       а на НЕравенство знаком меньше-больше <>
cursor.execute('UPDATE flowers SET price=99 WHERE id<>3')

vals = cursor.execute('SELECT price, name FROM flowers WHERE price < 100')
for v in vals:
    print(v)

# INSERT INTO flowers(name, price)
# VALUES (
#        ('rose',  100),
#        ('violet', 50),
#)  # id вставится сам с помощью функуции автоувеличения индекса

#        id      name    price
#         1      rose      100
#         2      viol       50
#

# SELECT name FROM flowers;
#
#        name
#        viol
#        rose

#tbls = cursor.execute('SELECT name FROM sqlite_schema')
#print(type(tbls))
#for t in tbls:
#    print(t)







