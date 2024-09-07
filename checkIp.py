#!/usr/bin/env python3

import requests
import json
import argparse

parser = argparse.ArgumentParser(description="Report IP findings from OTX, Tor, Shodan and IPinfo",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("ip")
parser.add_argument("-v","--verbose",action="store_true",help="Verbose output",default=False)
args = parser.parse_args()

TOR = False

sources = {
           "otx":"https://otx.alienvault.com/otxapi/indicators/ip/general/",
           "tor":"https://onionoo.torproject.org/details?search=",
           "shodan":"https://internetdb.shodan.io/",
           "ipinfo":"https://ipinfo.io/"
          }

for k,v in sources.items():
    r = requests.get(f"{v}{args.ip}")
    resp = json.dumps(r.json(),indent=4)

    if k == "tor":
        if "nickname" in r.text:
            TOR = True
        else:
            resp = "[x] Not a Tor relay"

    print(f"\n[+] Checking {k}...")
    print(f"\n" + "+="*40 + "\n")

    if TOR:
        print(f"\n[✔] {args.ip} is a Tor relay\n")
        if args.verbose:
            print(resp)
        TOR = False
    else:
        print(resp)

    print("\n" + "+="*40)
