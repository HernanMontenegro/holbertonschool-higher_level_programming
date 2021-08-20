#!/usr/bin/python3
''' Module 10 '''

import requests
import sys

if __name__ == '__main__':
    usr_name = sys.argv[1]
    usr_pass = sys.argv[2]
    url = 'https://api.github.com/user'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    req = requests.post(url, auth=(usr_name, usr_pass), headers=headers)
    print(req.json().get('id'))
