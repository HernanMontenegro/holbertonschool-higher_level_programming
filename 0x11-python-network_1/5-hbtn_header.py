#!/usr/bin/python3
''' Module 5 '''

import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get('x-request-id'))
