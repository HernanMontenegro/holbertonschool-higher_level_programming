#!/bin/bash
# Size in bytes
curl -sI 0.0.0.0:5000 | grep 'Content-Length' | cut -d ' ' -f2
