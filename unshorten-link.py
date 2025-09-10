#!/usr/bin/env python3

import requests
import sys

url = sys.argv[1]

# Only share.google and lnkd.in handled at the moment. More to come, probably

# Handle share.google shortlinks
def share_google(url):
    """
    # This gets the real url by following the Location header
    # until requests gets a 200 OK.
    # The downside to this approach is you make contact
    # with that final system.

    r = requests.get(url, allow_redirects=True)
    print(r.url)
    """

    # This gets the real url w/o contacting
    # the final endpoint
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

# Handle LinkedIn shortlinks
def linked_in(url):
    r = requests.get(url)
    for ln in r.text.split('\n'):
        if 'extern' in ln:
            for ln in ln.split('"'):
                if ln.startswith('http'):
                    print(ln)


if __name__ == "__main__":
    if 'share.google' in url:
        share_google(url)
    if 'lnkd.in' in url:
        linked_in(url)
