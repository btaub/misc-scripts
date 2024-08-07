#!/usr/bin/env python3

import mmh3
import requests
import codecs
import sys

response = requests.get(f'{sys.argv[1]}')
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print(hash)
