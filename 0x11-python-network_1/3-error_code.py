#!/usr/bin/python3
''' Dynamic request error '''

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: " + str(e.code))
