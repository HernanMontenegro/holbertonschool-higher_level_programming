#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    hbtn_url = 'http://0.0.0.0:5000/search_user'
    q = ""
    data = {}
    req = None

    if (len(sys.argv) == 2):
        q = sys.argv[1]

    data = {'q': q}
    req = requests.post(hbtn_url, data=data)
    try:
        dic = req.json()

        if (len(dic) == 0):
            print("No result")
        else:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
    except Exception as e:
        print("Not a valid JSON")
