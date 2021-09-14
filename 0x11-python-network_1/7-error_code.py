#!/usr/bin/python3
''' Module 7 error code '''

import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])

    if (req.status_code >= 400):
        print("Error code: {:d}".format(req.status_code))
    else:
        print(req.text)
