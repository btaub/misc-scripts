#!/usr/bin/python3
'''
  Check liveliness of local DNS resolvers
'''

import subprocess
import random
import argparse
import string
import re

parser = argparse.ArgumentParser(description="Check if local resolvers are responding to queries",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-v","--verbose",action="store_true",help="Verbose output",default=False)
args = parser.parse_args()


sites_list = []
sites = 'top-sites.txt' # List of FQDNs that should always be resolvable
servers = ['10.10.10.2',
           '10.10.10.22',
           '10.10.10.222']

with open(sites,'r') as f:
    for ln in f:
        sites_list.append(ln.strip('\n'))

site = random.choice(sites_list)
print(f'Testing against: {site}')

# Check response for presense of numbers. If no numbers are present, the op failed
def is_up(res):
    for x in string.digits:
        if re.search(x, res):
            return True

    return False

for ns in servers:
    res = subprocess.getoutput(f'dig +timeout=1 +short @{ns} {site}')
    ns_status = is_up(res)

    if ns_status:
        print(f'[ + ] {ns.ljust(15)} status: up ')
        if args.verbose:
            res = res.split('\n')
            print(f'resolved IPs: {res}')
    else:
        print(f'[ x ] {ns.ljust(15)} status: down ')
        if args.verbose:
            print(f'error: {res}')


'''
  Expected output:

$ ./test-local-dns.py -v
Testing against: newyorker.com
[ + ] 10.10.10.2     status: up
resolved IPs: ['166.117.251.134', '52.223.6.210']
[ x ] 10.10.10.22    status: down
error: ;; connection timed out; no servers could be reached
[ + ] 10.10.10.2222   status: up
resolved IPs: ['166.117.251.134', '52.223.6.210']

$ ./test-local-dns.py
Testing against: space.com
[ + ] 10.10.10.2    status: up
[ x ] 10.10.10.22    status: down
[ + ] 10.10.10.222   status: up
'''
