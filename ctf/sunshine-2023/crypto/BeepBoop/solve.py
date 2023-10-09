#!/usr/bin/env python3

import codecs

# this file is literally:
# beep boop beep beep....etc
infile = 'BeepBoop' 

# function grabbed from StackOverflow: https://stackoverflow.com/a/40559005
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

# replace beep and boop with 0 and 1 respectively, and strip spaces
with open(infile,'rb') as f:
    f = f.read().decode()
    f = f.replace('beep','0')
    f = f.replace('boop','1')
    f = f.replace(' ','')
#print(f)

# below converts the binary to:
# fha{rkgrezvangr-rkgrezvangr-rkgrezvangr}
f = decode_binary_string(f)

# convert the rot13 to the flag
f = codecs.encode(f, 'rot_13')
print(f)

# sun{exterminate-exterminate-exterminate}
