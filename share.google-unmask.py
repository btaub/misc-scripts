#!/usr/bin/env python3

import requests
import sys

url = sys.argv[1]

"""
# This gets the real url by following the Location header
# until requests gets a 200 OK.
# The downside to this approach is you make contact
# with that final system.

r = requests.get(url, allow_redirects=True)
print(r.url)
"""

# This gets the real url w/o contacting the final endpoint
while True:
    try:
        if not "share.google" in url:
            print(url)
            break
        r = requests.get(url, allow_redirects=False)
        if r.headers['Location']:
            url = r.headers['Location']

    except:
        break

