#!/usr/bin/python3
''' 100 module '''

import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    name = sys.argv[2]
    url = 'https://api.github.com/repos/'+ repo +'/'+ name +'/commits'
    req = requests.get(url)
    comm = req.json()

    for it in comm[:10]:
        print(it.get('sha') + ': ' + it.get('author').get('login'))
