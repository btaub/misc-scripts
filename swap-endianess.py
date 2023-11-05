#! /usr/bin/env python3

import sys

orig_str = sys.argv[1].encode()

m = len(orig_str[2:])
n = len(orig_str)

new_str = ''
input_len = int(len(orig_str.decode())) // 2

for _ in range(input_len):
    new_str += orig_str[m:n].decode()
    m -= 2
    n -= 2

print(f'input:  {orig_str.decode()}')
print(f'output: {new_str}')

'''
input:  EFBEADDE
output: DEADBEEF

input:  FEE1DEAD
output: ADDEE1FE
'''
