#!/usr/bin/python3

import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    cursor = db.cursor()

    sql = "SELECT c.id, c.name, s.name FROM cities c INNER JOIN states s "
    sql += "ON s.id = c.state_id;"

    cursor.execute(sql)

    data = cursor.fetchone()

    while (data):
        print(data)
        data = cursor.fetchone()

    db.close()


if __name__ == "__main__":
    main()
