#!/usr/bin/env python3

import ssl
import sys
import argparse
from cryptography import x509

parser = argparse.ArgumentParser(description="Quick and dirty way to check for an RDP listener",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("ip")
parser.add_argument("-v","--verbose",action="store_true",help="Verbose output",default=False)
args = parser.parse_args()

HOSTNAME = args.ip
PORT     = 3389
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
# output and type of cert.subject looks like this:
# <Name(CN=DESKTOP-01AB23C)>
# <class 'cryptography.x509.name.Name'>

# Clean up output. Could use some improvement
cert_subject = f"{cert.subject}"
cert_subject = cert_subject.split("(")[1].split(")")[0]
print(f"{HOSTNAME},{cert_subject}")

