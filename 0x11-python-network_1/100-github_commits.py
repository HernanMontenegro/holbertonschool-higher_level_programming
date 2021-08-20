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

    last_indx = len(comm) - 1

    for i in range(last_indx, last_indx - 11, -1):
        it = comm[i]
        print(it.get('sha') + ': ' + it.get('author').get('login'))
