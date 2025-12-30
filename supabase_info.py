#!/usr/bin/python3
'''
  Retrieve endpoint info from a supabase-based site
'''

import requests
import urllib3
import json
import sys
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
PROXY = {"https":"http://localhost:8080"}
SITE  = sys.argv[1]

# Get supabase db url and jwt from site index-*.js
def get_sb_info():
    r = requests.get(f'https://{SITE}', proxies=PROXY, verify=False)

    for ln in r.text.split('\n'):
        idx_file = re.search(r'/.+/index-.+.js', ln)
        if idx_file:
            js_index = f"https://{SITE}{idx_file[0]}"
            print(f"index file: {js_index}")
            r = requests.get(js_index, proxies=PROXY, verify=False)

            # parse the file for what we need
            for ln in r.text.split('"'):
                if re.search(r'.supabase.co', ln):
                    sb_site = ln
                    print(f"sb_site: {sb_site}")
                if re.search(r'^ey', ln):
                    sb_token = ln
                    print(f"sb_token: {sb_token}")

    return(sb_site, sb_token)

# Get endpoints
def get_sb_paths(sb_site, sb_token):
    r = requests.get(f'{sb_site}/rest/v1/', proxies=PROXY, verify=False,
                     headers={'apikey':f'{sb_token}',
                              'Authorization Bearer':f'{sb_token}'})

    schema_output_file = f'{sb_site.split("/")[2]}_root.json'

    with open(schema_output_file,'w') as f:
        f.write(json.dumps(r.json(), indent=4))

    paths = []

    print("\nPaths:\n")
    with open(schema_output_file,'r') as f:
        for ln in f:
            if re.search(r'\"/.[Aa-zZ, 0-9].+', ln):
                ln = ln.split('"')
                paths.append(ln[1])
                print(ln[1])

    return sorted(set(paths))

# Return the size of endpoint responses
def get_sb_path_lengths(sb_site, sb_token, paths):
    for path in paths:
        if 'rpc' not in path:
            endpoint = f'{sb_site}/rest/v1{path}'
            r = requests.get(f'{endpoint}', proxies=PROXY, verify=False,
                                headers={'apikey':f'{sb_token}',
                               'Authorization Bearer':f'{sb_token}'})

            print(f'{path}: {len(r.text)}')


sb_site, sb_token = get_sb_info()
paths = get_sb_paths(sb_site, sb_token)
print("\nTesting endpoint length...\n")
get_sb_path_lengths(sb_site, sb_token, paths)
