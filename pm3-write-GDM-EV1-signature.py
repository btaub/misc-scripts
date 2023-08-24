#!/usr/bin/env python3

import os
import sys
import subprocess
import shlex

'''
    This script converts the MFC EV1 signature sector to csetblk commands

    [usb] pm3 --> hf mf rdsc -s 17 -k 4B791BEA7BCC -b
    
    [=]   # | sector 17 / 0x11                                | ascii
    [=] ----+-------------------------------------------------+-----------------
    [=]  68 | 48 33 57 42 31 36 08 27 22 9F C7 00 00 00 00 00 | H3WB16.'".......
    [=]  69 | 53 44 B4 8D C1 CE A4 9D 7E D1 FE CF 08 16 5A 2A | SD......~.....Z*
    [=]  70 | 14 0C B5 F5 41 EC 50 B2 D3 CC BF F8 E1 ED 43 9D | ....A.P.......C.
    [=]  71 | 00 00 00 00 00 00 70 F0 F8 69 00 00 00 00 00 00 | ......p..i......

'''
GREEN = '\033[5;32m'
RED   = '\033[;31m'
NORM  = '\033[;m'
DEBUG = False

'''
    Block 71 comes back as zeroes, and the real
    data is static for EVERY EV1 card that exists, so...
'''
block_71  = '75CCB59C9BED70F0F8694B791BEA7BCC'

pm3_path = '/usr/local/bin/'
pm3_cmd  = shlex.split('./pm3 -c \"hf mf rdsc -s 17 -k 4B791BEA7BCC -b\"')
os.chdir(pm3_path)

try:
    res = subprocess.check_output(pm3_cmd)
except subprocess.CalledProcessError:
    print(RED + "\nCheck for open proxmark sessions and try again\n")
    sys.exit(-1)

res = res.decode()

if 'Auth error' in res:
    print(RED + '\nNot a MFC EV1 card\n')
    sys.exit(-1)

if 'Can\'t select' in res:
    print(RED + '\nCard not present\n')
    sys.exit(-1)

for line in res.split('\n'):
    if DEBUG:
        print(line)
    if '68 |' in line:
        block_68 = line.split('|')[1].replace(" ","")
    if '69 |' in line:
        block_69 = line.split('|')[1].replace(" ","")
    if '70 |' in line:
        block_70 = line.split('|')[1].replace(" ","")

print("\nCommands to write signature:\n" + GREEN)
print("hf mf csetblk -b 4 -d %s" % block_68)
print("hf mf csetblk -b 5 -d %s" % block_69)
print("hf mf csetblk -b 6 -d %s" % block_70)
print("hf mf csetblk -b 7 -d %s" % block_71)
print(NORM)
print("Config for GDM card (turns it into Gen 1a):\n")
print(GREEN + "hf mf gdmsetcfg -d 7AFF000000005A0000005A5A005A0008\n")

'''Output:

    % ./pm3-write-GDM-EV1-signature.py

    Commands to write signature:

    hf mf csetblk -b 4 -d 4833574231360827229FC70000000000
    hf mf csetblk -b 5 -d 5344B48DC1CEA49D7ED1FECF08165A2A
    hf mf csetblk -b 6 -d 140CB5F541EC50B2D3CCBFF8E1ED439D
    hf mf csetblk -b 7 -d 75CCB59C9BED70F0F8694B791BEA7BCC

    Config for GDM card (turns it into Gen 1a):

    hf mf gdmsetcfg -d 7AFF000000005A0000005A5A005A0008

'''
