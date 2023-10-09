#! /usr/bin/env python3

# solve script for sunshineCTF 2023 SimonProgrammer 1

import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initial request for getting cookie and answer data
r = requests.get('https://simon1.web.2023.sunshinectf.games/frequencies', verify=False)

# We need this data for the post
get_cookie = r.headers['Set-Cookie']
answer     = json.loads(r.text)

# example answer data:
# {'frequencies': ['/static/60.wav', '/static/8000.wav', '/static/9000.wav', '/static/6000.wav', '/static/1000.wav', '/static/2000.wav', '/static/7000.wav', '/static/3000.wav', '/static/2000.wav', '/static/8000.wav', '/static/9000.wav', '/static/1000.wav', '/static/6000.wav', '/static/8000.wav', '/static/2000.wav', '/static/8000.wav', '/static/7000.wav', '/static/4000.wav', '/static/7000.wav', '/static/9999.wav', '/static/5000.wav', '/static/60.wav', '/static/6000.wav', '/static/9000.wav', '/static/60.wav', '/static/5000.wav', '/static/8000.wav', '/static/8000.wav', '/static/6000.wav', '/static/9000.wav']}

# Clean up data we're returning:
payload = []

for k,v in answer.items():
    for freq in v:
        freq = freq.replace("/static/","")
        freq = freq.replace(".wav","")
        freq = int(freq) # probably not needed
        payload.append(freq)

# generate response data from get, has to be the list cast as string
# sample:
# <class 'str'>
# [4000, 1000, 9000, 3000, 2000, 60, 9999, 9000, 2000, 2000, 4000, 5000, 9000, 7000, 7000, 5000, 4000, 9000, 7000, 9999, 60, 9000, 5000, 8000, 7000, 4000, 7000, 2000, 4000, 4000]

payload = str(payload)
headers = {'Content-Type':'application/json','Cookie':get_cookie,'Accept': 'application/json'}

# initial/bad post data response: 
#    {"msg":"format: [frequency, frequency, frequency...]"}
# next response without cookie: 
#    {"msg":"Send cookies pls, cannot haz flag \ud83c\udf6a\ud83c\udf6a\ud83c\udf6a\ud83e\udd60."}
# other response with cookie and empty list: 
#     {"msg":"Not quite."}

# send the right response to get the flag
p = requests.post('https://simon1.web.2023.sunshinectf.games/flag',
                  data=payload, verify=False, headers=headers)

print("\n{}\n".format(p.json()['msg']))

# sun{simon_says_wait_that_was_a_mistake_what_do_you_mean_i_gave_all_the_frequencies}
