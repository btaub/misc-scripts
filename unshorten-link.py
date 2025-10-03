#!/usr/bin/env python3

import requests
import sys

url = sys.argv[1]
checked = False

"""
Supported:
    share.google
    lnkd.in
    bit.ly
    tinyurl.com
    ... and other services that rely on Location-header redirs
"""

# share.google
def share_google(url):
    while True:
        try:
            r = requests.get(url, allow_redirects=False)
            if "share.google" in url:
                 url = r.headers['Location']
            else:
                 return(url)
                 break

        except:
           return("something went wrong")
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
    # Specify scheme if missing
    if not url.startswith("https://"):
        url = f"https://{url}"
    # Fix copy-paste errors
    if url.endswith("/"):
        url = url.rstrip("/")
    if 'share.google' in url:
        res = share_google(url)
        checked = True
    # LinkedIn rarely redirects using a Location header, but mostly uses embedded links
    if 'lnkd.in' in url:
        res = head_req(url)
        if not res:
            res = linked_in(url)
        checked = True
    # And the rest of them
    if not checked:
        res = head_req(url)

    print(res)
