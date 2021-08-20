#!/usr/bin/python3
''' Module 0 '''

import requests

if __name__ == "__main__":
    hbtn_url = 'https://intranet.hbtn.io/status'
    req = requests.get(hbtn_url)
    cont = req.text
    print("Body response:")
    print("\t- type: " + str(type(cont)))
    print("\t- content: " + str(cont))
