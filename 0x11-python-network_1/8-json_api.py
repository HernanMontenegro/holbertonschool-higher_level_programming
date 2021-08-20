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

    resp_str = req.text[:-1]
    vals = resp_str.split(',')
    return_dict = {}

    if (len(vals) == 1):
        print("No result")
        exit()

    for i in range(0, len(vals)):
        k_v = vals[i].split(':')
        if (len(k_v) != 2):
            print("Not a valid JSON")
            exit()
        for j in range(0, len(k_v)):
            k_v[j] = k_v[j].replace('"', '').replace('{', '').replace('}', '')
        return_dict[k_v[0]] = k_v[1]

    print("[{}] {}".format(return_dict['id'], return_dict['name']))
