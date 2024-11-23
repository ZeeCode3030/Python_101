# this program takes a request from the link and returns the songs of the name 
# put as a command line argument e.g celine dion

import json
import requests
import sys

if len(sys.argv) == 2 :
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o['results']:
    print(result['trackName'])
# use system.py to improve the logic later 