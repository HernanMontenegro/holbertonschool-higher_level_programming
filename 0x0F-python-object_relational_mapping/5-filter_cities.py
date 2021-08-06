#!/usr/bin/python3

import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    cursor = db.cursor()

    result = ""
    sql = "SELECT c.id, c.name FROM cities c INNER JOIN states s "
    sql += "ON s.id = c.state_id WHERE s.name = ('{}')".format(argv[4])

    cursor.execute(sql)

    data = cursor.fetchone()

    while (data):
        result += data[1] + ", "
        data = cursor.fetchone()

    result = result[: len(result) - 2]

    print(result)

    db.close()


if __name__ == "__main__":
    main()
