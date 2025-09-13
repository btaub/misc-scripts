#! /usr/bin/env python3

import sys
import os
import requests
import json

DOMAIN     = f'{sys.argv[1]}'
SHODAN_KEY = '__FILL_ME_IN__'
C99_KEY    = '__FILL_ME_IN__'
c99_url    = f'https://api.c99.nl/subdomainfinder?key={C99_KEY}&domain={DOMAIN}'
otx_url    = f'https://otx.alienvault.com/otxapi/indicators/domain/passive_dns/{DOMAIN}'
shodan_url = f'https://api.shodan.io/dns/domain/{DOMAIN}?key={SHODAN_KEY}'

def shodan(DOMAIN):
    SUBDOMAINS = []

    res = requests.get(shodan_url)

    for k,v in res.json().items():
        if k == 'data':
            for itm in v:
                for k,v in itm.items():
                    if k == 'subdomain':
                        SUBDOMAINS.append(v)
    SUBDOMAINS = sorted(set(SUBDOMAINS))

    with open(f'{DOMAIN}_shodan.txt','a') as f:
        for host in SUBDOMAINS:
            f.write(f'{host}.{DOMAIN}\n')

    return(SUBDOMAINS)

def c99(DOMAIN):
    res = requests.get(c99_url)
    res = res.text.split('<br>')
    with open(f'{DOMAIN}_c99.txt','a') as f:
        for host in res:
            f.write(f'{host}\n')
    return(res)

def otx(DOMAIN):
    SUBDOMAINS = []

    res = requests.get(otx_url)
    res = res.json()

    for k,v in res.items():
        if k == 'passive_dns':
            for l in v:
                for k,v in l.items():
                    if k == 'hostname':
                        SUBDOMAINS.append(v)

    SUBDOMAINS = sorted(set(SUBDOMAINS))

    output = f'{DOMAIN}_otx.txt'

    if os.path.exists(output):
        os.rename(output,f'{output}-old')

    with open(output,'a+') as f:
        for host in SUBDOMAINS:
            f.write(f'{host}\n')

    return(SUBDOMAINS)

if __name__ == "__main__":
    otx_records    = otx(DOMAIN)
    shodan_records = shodan(DOMAIN)
    c99_records    = c99(DOMAIN)

    all_records = otx_records + shodan_records + c99_records
    all_records = sorted(set(all_records))
    all_file    = f'{DOMAIN}_all.txt'

    with open(all_file,'w') as f:
        for record in all_records:
            if record:
                f.write(f'{record}\n')
