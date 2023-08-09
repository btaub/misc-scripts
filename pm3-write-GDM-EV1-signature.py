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
    [=]  68 | 48 33 30 54 34 32 0A 41 21 AF 02 04 00 00 00 00 | H30T42.A!.......
    [=]  69 | 13 12 67 FF D5 4A 34 91 7F 62 2A 2C 03 DB 9B 55 | ..g..J4..b*,...U
    [=]  70 | 51 AB 3F 7D 0A 33 F0 7C F5 2B 3D 82 5A 39 0C E8 | Q.?}.3.|.+=.Z9..
    [=]  71 | 00 00 00 00 00 00 70 F0 F8 69 00 00 00 00 00 00 | ......p..i......
'''
GREEN = '\033[5;32m'
RED   = '\033[;31m'
NORM  = '\033[;m'
DEBUG = False

'''
    Line 71 comes back as zeroes, and the real
    data is static for EVERY EV1 card that exists, so...
'''
line_71  = '75CCB59C9BED70F0F8694B791BEA7BCC'

pm3_path = '/usr/local/bin/'
pm3_cmd  = shlex.split('./pm3 -c \"hf mf rdsc -s 17 -k 4B791BEA7BCC -b\"')
os.chdir(pm3_path)

try:
    res = subprocess.check_output(pm3_cmd)
except subprocess.CalledProcessError:
    print(RED + "\nCheck for open proxmark sessions and try again, doofus\n")
    sys.exit(-1)

if DEBUG:
    print(res)

res = res.decode()

if 'Auth error' in res:
    print(RED + '\nNot a MFC EV1 card\n')
    sys.exit(-1)

if 'Can\'t select' in res:
    print(RED + '\nCard not present\n')
    sys.exit(-1)

for line in res.split('\n'):
    if '68 |' in line:
        line_68 = line.split('|')[1].replace(" ","")
    if '69 |' in line:
        line_69 = line.split('|')[1].replace(" ","")
    if '70 |' in line:
        line_70 = line.split('|')[1].replace(" ","")

print("\nCommands to write signature:\n" + GREEN)
print("hf mf csetblk -b 4 -d %s" % line_68)
print("hf mf csetblk -b 5 -d %s" % line_69)
print("hf mf csetblk -b 6 -d %s" % line_70)
print("hf mf csetblk -b 7 -d %s" % line_71)
print(NORM)
print("Config for GDM card (turns it into Gen 1a):\n")
print(GREEN + "hf mf gdmsetcfg -d 7AFF000000005A0000005A5A005A0008\n")
