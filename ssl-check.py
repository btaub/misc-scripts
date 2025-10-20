#!/usr/bin/env python3

import ssl
import sys
import argparse
from cryptography import x509

parser = argparse.ArgumentParser(description="Quick and dirty way to check for an RDP listener",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("ip")
parser.add_argument("port")
parser.add_argument("-v","--verbose",action="store_true",help="Verbose output",default=False)
args = parser.parse_args()

HOSTNAME = args.ip
PORT     = args.port
context  = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

try:
    get_cert = ssl.get_server_certificate((HOSTNAME,PORT),timeout=1)
except Exception as e:
    if args.verbose:
        print(f"{HOSTNAME},[ERROR] {e}")
    sys.exit(-1)

cert = x509.load_pem_x509_certificate(get_cert.encode('latin-1'))

cert_subject = cert.subject.rfc4514_string()
print(f"{HOSTNAME},{cert_subject}")
