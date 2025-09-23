#!/usr/bin/env python3

import requests
import sys

url = sys.argv[1]

"""
Supported:
    share.google
    lnkd.in
    bit.ly
"""

# share.google
def share_google(url):
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
                return(url)
                break
            r = requests.get(url, allow_redirects=False)

            if r.headers['Location']:
                url = r.headers['Location']

        except:
           break

# LinkedIn
def linked_in(url):
    r = requests.get(url)
    for ln in r.text.split('\n'):
        if 'extern' in ln:
            for ln in ln.split('"'):
                if ln.startswith('http'):
                    return(ln)

# Generic location header-based HEAD request
def head_req(url):
    r = requests.head(url)
    try:
        res = r.headers['location']
    except:
        res = None

    return(res)

if __name__ == "__main__":
    if 'share.google' in url:
        res = share_google(url)
    if 'lnkd.in' in url:
        res = head_req(url)
        if not res:
            res = linked_in(url)
    if 'bit.ly' in url or 'tinyurl.com' in url:
        res = head_req(url)
        
    print(res)
