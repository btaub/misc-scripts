#!/usr/bin/env python3

'''
    Encrypt or decrypt HID iClass block 7 data.
    Similar to the proxmark3 "hf iclass [encrypt | decrypt]" commands
'''

#from Crypto.Cipher import DES3      # python3 pip -m install pycyptodome
from Cryptodome.Cipher import DES3   # python3 pip -m install pycryptodomex
import binascii
import argparse

'''
    Arguments
'''
parser = argparse.ArgumentParser(description="encrypt/decrypt HID iClass classic block 7 data, "
                                             "based off of the work done by RfidResearch group, and others "
                                 ,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-i","--input",  required=True, help="The data to encrypt/decrypt")
parser.add_argument("-a","--action", required=True, help="Encrypt or decrypt", choices=['enc','dec'])
args = parser.parse_args()

'''
    Key data from:
    github.com/RfidResearchGroup/proxmark3/tree/master/client/resources/iclass_decryptionkey.bin
'''
key = b'\xb4!,\xca\xb7\xed!\x0f{\x93\xd4Y9\xc7\xdd6'

'''
    Example data:
    encrypted block 7: 9F5A9326D3D49ECF
    plaintext block 7: 00000000055C5593
'''
def main(key, self):
    cipher = DES3.new(key, DES3.MODE_ECB)
    str_input = binascii.unhexlify(self.encode())

    if args.action == "enc":
        msg = cipher.encrypt(str_input)
        str_output = binascii.hexlify(msg)
        print("\nEncrypted: %s\n" % str_output.decode().upper())
    elif args.action == "dec":
        msg = cipher.decrypt(str_input)
        str_output = binascii.hexlify(msg)
        print("\nDecrypted: %s\n" % str_output.decode().upper())

    return

if __name__ == "__main__":
    main(key,args.input)
