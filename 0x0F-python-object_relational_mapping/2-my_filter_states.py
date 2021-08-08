#!/usr/bin/python3
''' 2 - module '''

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name = '{}'".format(argv[4])

    cursor.execute(sql)

    data = cursor.fetchone()

    while (data):
        print(data)
        data = cursor.fetchone()

    db.close()
