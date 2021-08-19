#!/bin/bash
# Size in bytes
curl -sI "$1" | grep 'Content-Length' | cut -d ' ' -f 2
