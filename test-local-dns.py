#!/usr/bin/python3
'''
  Check liveliness of local DNS resolvers
'''

import subprocess
import random
import argparse
import shlex

parser = argparse.ArgumentParser(description="Check if local resolvers are responding to queries",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-v","--verbose",action="store_true",help="Verbose output",default=False)
args = parser.parse_args()

sites = [
         'space.com',
         'un.org',
         'who.int',
         'example.com',
         'ntp.org',
         'newyorker.com',
         'freebsd.org'
        ]

servers = [
           '10.10.10.2',
           '10.10.10.22',
           '10.10.10.222'
          ]

site = random.choice(sites)
print(f'Testing against: {site}')

# Assume dig is installed and in the path.
for ns in servers:
    try:
        res = subprocess.check_output(shlex.split(f'dig +timeout=1 +short @{ns} {site}'))
        print(f'[ + ] {ns.ljust(15)} status: up ')
        if args.verbose:
            res = res.decode('latin-1')
            res = res.strip('\n')
            res = res.split('\n')
            print(f'resolved IPs: {res}')

    except subprocess.CalledProcessError as e:
        print(f'[ x ] {ns.ljust(15)} status: down ')
        if args.verbose:
            print(f'error: {e}')

'''
  Expected output:

$ ./test-local-dns.py -v
Testing against: newyorker.com
[ + ] 10.10.10.2     status: up
resolved IPs: ['166.117.251.134', '52.223.6.210']
[ x ] 10.10.10.22    status: down
error: Command '['dig', '+timeout=1', '+short', '@10.10.10.22', 'ntp.org']' returned non-zero exit status 9.
[ + ] 10.10.10.222   status: up
resolved IPs: ['166.117.251.134', '52.223.6.210']

$ ./test-local-dns.py
Testing against: space.com
[ + ] 10.10.10.2    status: up
[ x ] 10.10.10.22    status: down
[ + ] 10.10.10.222   status: up
'''
