#!/usr/bin/python3

import requests
import sys

if __name__ == '__main__':
    usr_name = sys.argv[1]
    usr_pass = sys.argv[2]
    headers = {'Accept': 'application/vnd.github.v3+json'}
    url = 'https://api.github.com/user'

    req = requests.get(url, auth=(usr_name, usr_pass), headers=headers)
    print(req.json().get('id'))
