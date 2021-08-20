#!/usr/bin/python3
''' Dynamic email request '''

import urllib.request
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    url = sys.argv[1]
    email = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=email)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
