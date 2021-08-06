#!/usr/bin/python3

import MySQLdb
from sys import argv

db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

cursor = db.cursor()

sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC;"

cursor.execute(sql)

data = cursor.fetchone()

while (data):
    print(data)
    data = cursor.fetchone()

db.close()