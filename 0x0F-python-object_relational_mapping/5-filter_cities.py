#!/usr/bin/python3

import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    cursor = db.cursor()

    result = ""
    sql = "SELECT c.name FROM cities c INNER JOIN states s "
    sql += "ON s.id = c.state_id WHERE s.name = ('{}')".format(argv[4])

    cursor.execute(sql)

    data = cursor.fetchone()

    for i in range(0, cursor.rowcount):
        result += data[0]
        if (i != cursor.rowcount - 1):
            result += ", "
        data = cursor.fetchone()

    print(result)

    db.close()


if __name__ == "__main__":
    main()
