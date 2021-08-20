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
    last_ones = []

    for i in range(0, len(comm)):
        if (i == 10):
            break
        last_ones.append(comm[i])

    for i in range(0, len(last_ones)):
        it = last_ones[i]
        print(it.get('sha') + ': ' + it.get('author').get('login'))
