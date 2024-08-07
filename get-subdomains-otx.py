#!/usr/bin/env python3

import requests
import json
import sys
import os

VERBOSE = False
result = []

otx_url = f'https://otx.alienvault.com/otxapi/indicators/domain/passive_dns/{sys.argv[1]}'

r = requests.get(otx_url)
r = json.loads(r.text)

for k,v in r.items():
    if k == 'passive_dns':
        for l in v:
            for k,v in l.items():
                if k == 'hostname':
                    result.append(v)

result = sorted(set(result))

output = f'{sys.argv[1]}.txt'

if os.path.exists(output):
    os.rename(output,f'{output}-old')

with open(output,'a+') as f:
    for host in result:
        f.write(f'{host}\n')

        if VERBOSE:
            print(hosts)

