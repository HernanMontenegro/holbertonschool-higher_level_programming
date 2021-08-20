#!/usr/bin/python3
''' 100 module '''

import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    name = sys.argv[2]
    url = 'https://api.github.com/repos/' + name + '/' + repo + '/commits'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    req = requests.get(url, headers=headers)

    comm = req.json()

    for c in comm[:10]:
        print(c.get('sha') + ': ' + c.get('commit').get('author').get('name'))
