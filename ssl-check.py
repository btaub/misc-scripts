#!/usr/bin/env python3

import ssl
import sys
import argparse
from cryptography import x509

parser = argparse.ArgumentParser(description="Quick and dirty way to check for an SSL listener",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-i","--ip", required=False, help="IPv4 address to check, e.g. 4.2.2.2")
parser.add_argument("-p", "--port", required=False, default=443)
parser.add_argument("-f","--file",  required=False, help="File containing a list of IPs")
parser.add_argument("-v","--verbose",action="store_true",help="Verbose output",default=False)
args = parser.parse_args()

if not args.ip and not args.file:
    parser.print_help()
    sys.exit(-1)

def main(self):

    if args.file:
        HOSTNAME = self
    else:
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

if __name__ == "__main__":
    if args.file:
        with open(args.file, 'r') as f:
            for HOSTNAME in f.read:
                HOSTNAME = HOSTNAME.strip('\n')
                print(f"DBG: {HOSTNAME}")
                main(HOSTNAME)
    else:
        main(args.ip)
