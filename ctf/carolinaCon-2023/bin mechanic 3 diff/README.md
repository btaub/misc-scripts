# Challenge text:
Binary files bin3.1 and bin3.2 differ

---

Took the easy road and used bindiff.py to output the flag:

```shell
% python3 bindiff.py -l artifcats/bin3.1 artifcats/bin3.2
Result of comparison: content
File 1 length:  10280096
File 2 length:  10280096
Num. differences:  21
offset differs: 0x618
List of differences:
offset 0x00000618: 0x66 != 0x00 ('f' !=   0)
offset 0x0001476c: 0x6c != 0x00 ('l' !=   0)
offset 0x0016384c: 0x61 != 0xfc ('a' != 'ü')
offset 0x0017ce32: 0x67 != 0x00 ('g' !=   0)
offset 0x00275de5: 0x7b != 0xde ('{' != 'Þ')
offset 0x002f52d8: 0x77 != 0x3c ('w' != '<')
offset 0x003381e1: 0x68 != 0x02 ('h' !=   2)
offset 0x003aaa28: 0x34 != 0x8c ('4' != '')
offset 0x003c58a9: 0x74 != 0x00 ('t' !=   0)
offset 0x00435c18: 0x35 != 0x00 ('5' !=   0)
offset 0x0051392f: 0x5f != 0x00 ('_' !=   0)
offset 0x005c02b4: 0x74 != 0x00 ('t' !=   0)
offset 0x006a0ef5: 0x68 != 0x00 ('h' !=   0)
offset 0x0070fd78: 0x33 != 0x00 ('3' !=   0)
offset 0x00749434: 0x5f != 0x00 ('_' !=   0)
offset 0x007be138: 0x64 != 0x10 ('d' !=  16)
offset 0x007d9a36: 0x31 != 0x64 ('1' != 'd')
offset 0x008295f9: 0x66 != 0x00 ('f' !=   0)
offset 0x00874d79: 0x66 != 0x00 ('f' !=   0)
offset 0x00902eb9: 0x3f != 0x00 ('?' !=   0)
offset 0x0096b97a: 0x7d != 0x39 ('}' != '9')
Elapsed time:  00:00:01

```
