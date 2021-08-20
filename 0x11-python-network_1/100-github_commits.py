#!/usr/bin/python3
''' 100 module '''

import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, name)
    headers = {'Accept': 'application/vnd.github.v3+json'}
    req = requests.get(url, headers=headers)
    comm = req.json()

    for it in comm[:10]:
        print(it.get('sha') + ': ' + it.get('author').get('login'))
