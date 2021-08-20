#!/bin/bash
# displays the body of the response
curl -s -F "email=hr@holbertonschool.com" -F "subject=I will always be here for PLD" -X POST "$1"
