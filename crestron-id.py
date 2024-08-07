#!/usr/bin/python3

import socket
import sys

HOST = f'{sys.argv[1]}'
PORT = 41794
PAYLOAD =  b'\x14\x00\x00\x00\x01\x04\x00\x03\x00\x00'
PAYLOAD += b'\x00' * 256

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', PORT))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(1)
s.sendto(PAYLOAD,(HOST, PORT))
response = server_socket.recvfrom(1024)
response = response[0].split(b'\x00')

for x in response:
    x = x.decode(errors='ignore')
    if x:
        if not x == '\x15' and not x == '\x01\x84':
            print(f"{x}")

'''Sample output:

TSS-752-00107F941EAB
TSS-752 [v1.002.0013 (March 03 2016), #0100257D]

'''
