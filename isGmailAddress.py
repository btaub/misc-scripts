#!/usr/bin/env python3

import requests
import argparse

parser = argparse.ArgumentParser(description="Check GMail address validity",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-e","--email",help="A single address to check")
parser.add_argument("-f","--file",help="A CRLF delimited set of addresses to check")
parser.add_argument("-v","--verbose",action="store_true",help="Verbose output",default=False)
args = parser.parse_args()

email =  args.email
addr  = "https://mail.google.com/mail/gxlu?email={}"

def check_email(email):
    r = requests.get(addr.format(email))

    if args.verbose:
        print(f"\n[!] VERBOSE: {r.headers}\n")

    if "Set-Cookie" in r.headers:
        return(f"[✔] {email} is a REGISTERED GMail address")
    else:
        return(f"[x] {email} is an INVALID GMail address")

if __name__ == "__main__":

    if args.file:
        with open(args.file,'r') as f:
            for email in f:
                print(check_email(email.strip()))

    else:
        if email:
            print(check_email(email))
        else:
            parser.print_help()

''' Output:

    % ./isGmailAddress.py -e fooasdfasdc@google.com
    [x] fooasdfasdc@google.com is an INVALID GMail address

    % ./isGmailAddress.py -e foo@google.com
    [✔] foo@google.com is a REGISTERED GMail address
'''
