#!/usr/bin/env python3

import sys

inp = f"0x{sys.argv[1]}"
inp = eval(inp)

print(bin(inp)[2:])
