#!/usr/bin/env python3
'''
  Report findings from IP reputation/info sites
'''

import json
import argparse
import requests

parser = argparse.ArgumentParser(description="Report IP findings from OTX, Tor, Shodan and IPinfo",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("ip")
parser.add_argument("-v","--verbose",action="store_true",help="Verbose output",default=False)
args = parser.parse_args()

ABUSEIP_HEADERS = {'Key':'__ ENTER ABUSEIPDB KEY HERE __'}
is_tor = False

sources = {
           "otx":"https://otx.alienvault.com/otxapi/indicators/ip/general/",
           "tor":"https://onionoo.torproject.org/details?search=",
           "shodan":"https://internetdb.shodan.io/",
           "ipinfo":"https://ipinfo.io/",
           "abuseipdb":"https://api.abuseipdb.com/api/v2/check?maxAgeInDays=90&ipAddress="
          }

for k,v in sources.items():
    print(f"\n[+] Checking {k}...")

    if k == 'abuseipdb':
        r = requests.get(f"{v}{args.ip}",headers=ABUSEIP_HEADERS)
        for k_abuse_ipdb,v_abuse_ipdb in r.json().items():
            if v_abuse_ipdb['totalReports'] > 0:
                print('\nAbuseIPDB reports found: '
                     f'https://www.abuseipdb.com/check/{args.ip}')

    else:
        r = requests.get(f"{v}{args.ip}")
    resp = json.dumps(r.json(),indent=4)

    if k == "tor":
        if "nickname" in r.text:
            is_tor = True
        else:
            resp = "[x] Not a Tor relay"

    print("\n" + "+="*40 + "\n")

    if is_tor:
        print(f"\n[✔] {args.ip} is a Tor relay\n")
        print("Check here for more detail:")
        print(f"https://metrics.torproject.org/rs.html#search/{args.ip}")
        if args.verbose:
            print(resp)
        is_tor = False
    else:
        print(resp)

    print("\n" + "+="*40)
