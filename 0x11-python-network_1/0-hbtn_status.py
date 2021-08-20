#!/usr/bin/python3
''' Module 0 '''

import urllib.request

if __name__ == "__main__":
    hbtn_url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(hbtn_url) as res:
        cont = res.read()
        print("Body response:")
        print("\t- type: " + str(type(cont)))
        print("\t- content: " + str(cont))
        print("\t- utf8 content: " + cont.decode("utf-8"))
