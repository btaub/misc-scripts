# Mathemetician

### category: scripting
## clue

```
I heard you were good at math...

Mind helping me out?

`challenges.carolinacon.org:8003`
```

## flag

```python
#!/usr/bin/env python3

from pwn import *
import socket
import time

host = 'challenges.carolinacon.org'
port =  8003

# 'what is 5 + 10?'
n = 0
s = remote(host, port)

while 1:
    resp = s.recv(1024)

    print("RESP1: %s" % resp)
    resp = resp.replace(b'what is ',b'')
    resp = resp.strip()

    ans = eval(resp)
    print(f"ANS: {ans}, {n}")
    s.sendline(str(ans).encode())

    n += 1
    time.sleep(.01)

'''
ANS: 31, 994
RESP1: b'what is 16 + 55\n'
ANS: 71, 995
RESP1: b'what is 46 + 96\n'
ANS: 142, 996
RESP1: b'what is 38 + 139\n'
ANS: 177, 997
RESP1: b'what is 88 + 134\n'
ANS: 222, 998
RESP1: b'what is 37 + 99\n'
ANS: 136, 999
RESP1: b'ccg{1_4lw4ys_kn3w_y0u_could_do_it}\n'

'''
```
---

# Mathemagician

### category: scripting

## clue

```
Maybe you _are_ a mathemetician, but what if I throw some magic in...

`challenges.carolinacon.org:8004`
```

## flag

```python
#!/usr/bin/env python3

from pwn import *

host = 'challenges.carolinacon.org'
port = 8004
n = 0

# example initial server response:
# what is 58 + 69

s = remote(host, port)

while 1:
    resp = s.recvline()
    #print(f"RESP: {resp}")
    if b'what is' not in resp:
        print(f"WIN??? {resp}")
        success(s.recvall().decode())
        break
    resp = resp.replace(b'what is', b'')
    resp = resp.strip()

    # This part could be done better by 
    # someone that knows what they're doing...
    if b'zero' in resp:
        resp = resp.replace(b'zero',b'0')
    if b'one' in resp:
        resp = resp.replace(b'one',b'1')
    if b'two' in resp:
        resp = resp.replace(b'two',b'2')
    if b'three' in resp:
        resp = resp.replace(b'three',b'3')
    if b'four' in resp:
        resp = resp.replace(b'four',b'4')
    if b'five' in resp:
        resp = resp.replace(b'five',b'5')
    if b'six' in resp:
        resp = resp.replace(b'six',b'6')
    if b'seven' in resp:
        resp = resp.replace(b'seven',b'7')
    if b'eight' in resp:
        resp = resp.replace(b'eight',b'8')
    if b'nine' in resp:
        resp = resp.replace(b'nine',b'9')

    # yes eval'ing blindly is awful practice but...
    # it's a ctf so whatever, it works
    ans = eval(resp)
    #print(f"SENT: {ans}")
    s.sendline(str(ans).encode())
    n += 1
    print(f"Attempt: {n}")

'''
Attempt: 992
Attempt: 993
Attempt: 994
Attempt: 995
Attempt: 996
Attempt: 997
Attempt: 998
Attempt: 999
Attempt: 1000
WIN??? b'count:\n'
[+] Receiving all data: Done (48B)
[*] Closed connection to challenges.carolinacon.org port 8004
[+] 1000
    cc_ctf{what_are_you_some_k1nd_0f_w1z4rd?}

'''
```
![mathmagician](https://raw.githubusercontent.com/btaub/misc-scripts/refs/heads/master/ctf/carolinaCon-2024/images/mathmagician.png)
