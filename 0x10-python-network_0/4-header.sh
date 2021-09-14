#!/bin/bash
# displays the body of the response
curl -s -H "X-HolbertonSchool-User-Id":"98" -X GET "$1"
