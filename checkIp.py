#!/usr/bin/env python3

import requests
import sys
import json

''' TODO:
    1) Add logging option
    2) Change sys to argparse
'''

sources = {
           "otx":"https://otx.alienvault.com/otxapi/indicators/ip/general/",
           "shodan":"https://internetdb.shodan.io/",
           "ipinfo":"https://ipinfo.io/"
          }

for k,v in sources.items():
    r = requests.get("%s%s" % (v , sys.argv[1]))
    print("+="*40)
    print()
    print("  Checking %s..." % k)
    print()
    print("+="*40)
    print(json.dumps(r.json(),indent=4))
    print()
    print("+="*40)
