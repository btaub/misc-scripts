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

# This gets the real url w/o contacting
# with the final endpoint
while True:
    try:
        r = requests.get(url, allow_redirects=False)
        if not "share.google" in r.headers['Location']:
            print(f"Unmasked url: {r.headers['Location']}")
        if r.headers['Location']:
            url = r.headers['Location']

    except:
        break

