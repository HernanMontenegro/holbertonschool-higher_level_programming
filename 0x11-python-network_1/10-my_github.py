#!/usr/bin/python3

import requests
import sys

if __name__ == '__main__':
    usr_name = sys.argv[1]
    usr_pass = sys.argv[2]
    url = 'https://api.github.com/user'

    req = requests.get(url, auth=(usr_name, usr_pass))
    print(req.json().get('id'))
