#!/usr/bin/python3
''' 3 - module '''

import MySQLdb
from sys import argv


def main():
    ''' Main func '''
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name = ('{}')".format(argv[4])
    sql += " ORDER BY states.id ASC;"

    cursor.execute(sql)

    data = cursor.fetchone()

    while (data):
        print(data)
        data = cursor.fetchone()

    db.close()


if __name__ == "__main__":
    main()
