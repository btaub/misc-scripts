I didn't get this flag during the CTF, but looking at it now after getting more familiar with gdb it makes sense. There's a function named free that never gets called. Jump to it and it prints the flag that's obfuscated in code.

```gdb
┌──(kali㉿kali)-[~/Documents/CC-CTF-Online-3/pwn/strings]
└─$ ./strings
I've got no strings
To hold me down
To make me fret
To make me frown
I once had strings
But now I'm free
There are no strings on me

┌──(kali㉿kali)-[~/Documents/CC-CTF-Online-3/pwn/strings]
└─$ gdb -q strings
GEF for linux ready, type `gef' to start, `gef config' to configure
88 commands loaded and 5 functions added for GDB 13.2 in 0.00ms using Python engine 3.11
Reading symbols from strings...
(No debugging symbols found in strings)
gef➤  info functions -q
0x08049010  printf@plt
0x08049020  free
0x08049237  _start
0x08049d5c  a
0x08049d5e  b
0x08049d60  c
0x08049d62  d
0x08049d64  e
0x08049d66  f
0x08049d68  g
0x08049d6a  h
0x08049d6c  i
0x08049d6e  j
0x08049d70  k
0x08049d72  l
0x08049d74  m
0x08049d76  n
0x08049d78  o
0x08049d7a  p
0x08049d7c  q
0x08049d7e  r
0x08049d80  s
0x08049d82  t
0x08049d84  u
0x08049d86  v
0x08049d88  w
0x08049d8a  x
0x08049d8c  y
0x08049d8e  z
0x08049d90  A
0x08049d92  B
0x08049d94  C
0x08049d96  D
0x08049d98  E
0x08049d9a  F
0x08049d9c  G
0x08049d9e  H
0x08049da0  I
0x08049da2  J
0x08049da4  K
0x08049da6  L
0x08049da8  M
0x08049daa  N
0x08049dac  O
0x08049dae  P
0x08049db0  Q
0x08049db2  R
0x08049db4  S
0x08049db6  T
0x08049db8  U
0x08049dba  V
0x08049dbc  W
0x08049dbe  X
0x08049dc0  Y
0x08049dc2  Z
0x08049dc4  P0
0x08049dc6  P1
0x08049dc8  P2
0x08049dca  P3
0x08049dcc  P4
0x08049dce  P5
0x08049dd0  P6
0x08049dd2  P7
0x08049dd4  P8
0x08049dd6  P9
0x08049dd8  PO
0x08049dda  PU
0x08049ddc  PC
0x08049dde  PS
0x08049de0  PA
0x08049de2  PB
0xf7fcb1c0  _dl_signal_exception
0xf7fcb230  _dl_signal_error
0xf7fcb460  _dl_catch_exception
0xf7fcc5e0  _dl_debug_state
0xf7fcd770  _dl_exception_create
0xf7fcd860  _dl_exception_create_format
0xf7fcdbd0  _dl_exception_free
0xf7fcdd90  __nptl_change_stack_perm
0xf7fd3500  _dl_rtld_di_serinfo
0xf7fd5ef0  _dl_find_dso_for_object
0xf7fd75d0  _dl_fatal_printf
0xf7fd7dd0  _dl_mcount
0xf7fdb2f0  _dl_get_tls_static_info
0xf7fdb3d0  _dl_allocate_tls_init
0xf7fdb6a0  _dl_allocate_tls
0xf7fdb6e0  _dl_deallocate_tls
0xf7fdb990  __tls_get_addr
0xf7fdb9e0  ___tls_get_addr
0xf7fdde70  __tunable_get_val
0xf7fe0430  _dl_x86_get_cpu_features
0xf7fe07b0  _dl_audit_preinit
0xf7fe0860  _dl_audit_symbind_alt
0xf7fec560  __rtld_version_placeholder
0xf7fc8580  __kernel_vsyscall
0xf7fc85a0  __kernel_sigreturn
0xf7fc85b0  __kernel_rt_sigreturn
0xf7fc87b0  __vdso_gettimeofday
0xf7fc8af0  __vdso_time
0xf7fc8b40  __vdso_clock_gettime
0xf7fc8fb0  __vdso_clock_gettime64
0xf7fc9450  __vdso_clock_getres
0xf7fc94e0  __vdso_getcpu

gef➤  jump *free
The program is not being run.
gef➤  starti
Starting program: /home/kali/Documents/CC-CTF-Online-3/pwn/strings/strings

Program stopped.
0xf7fe3f20 in ?? () from /lib/ld-linux.so.2
[ Legend: Modified register | Code | Heap | Stack | String ]
─────────────────────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0x0
$ebx   : 0x0
$ecx   : 0x0
$edx   : 0x0
$esp   : 0xffffd320  →  0x00000001
$ebp   : 0x0
$esi   : 0x0
$edi   : 0x0
$eip   : 0xf7fe3f20  →   mov eax, esp
$eflags: [zero carry parity adjust sign trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x00
─────────────────────────────────────────────────────────────────────────────────────────── stack ────
0xffffd320│+0x0000: 0x00000001	 ← $esp
0xffffd324│+0x0004: 0xffffd4a8  →  "/home/kali/Documents/CC-CTF-Online-3/pwn/strings/s[...]"
0xffffd328│+0x0008: 0x00000000
0xffffd32c│+0x000c: 0xffffd4e1  →  "LC_TERMINAL_VERSION=3.4.21"
0xffffd330│+0x0010: 0xffffd4fc  →  "LANG=en_US.UTF-8"
0xffffd334│+0x0014: 0xffffd50d  →  "LC_TERMINAL=iTerm2"
0xffffd338│+0x0018: 0xffffd520  →  "USER=kali"
0xffffd33c│+0x001c: 0xffffd52a  →  "LOGNAME=kali"
───────────────────────────────────────────────────────────────────────────────────── code:x86:32 ────
   0xf7fe3f14                  lea    esi, [esi+eiz*1+0x0]
   0xf7fe3f1b                  lea    esi, [esi+eiz*1+0x0]
   0xf7fe3f1f                  nop
 → 0xf7fe3f20                  mov    eax, esp
   0xf7fe3f22                  sub    esp, 0xc
   0xf7fe3f25                  push   eax
   0xf7fe3f26                  call   0xf7fe4ae0
   0xf7fe3f2b                  add    esp, 0x10
   0xf7fe3f2e                  mov    edi, eax
───────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "strings", stopped 0xf7fe3f20 in ?? (), reason: STOPPED
─────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0xf7fe3f20 → mov eax, esp
──────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  jump *free
Continuing at 0x8049020.
flag{n0_stR1ng5_0n_M3eE}[Inferior 1 (process 711638) exited with code 01]
gef➤

```
