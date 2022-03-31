import argparse
import sys 
from .cipher import cipher as true_c

def cipher():
    key = input("Please give the ciphering key:\n")
    ptext = input("Please give the clear text to cipher:\n")
    print(true_c(key,ptext))
    
def entrypoint():  # console entry point
    
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_cipher = subparsers.add_parser('cipher',help="Ciphers the given text with the given key")
    parser_cipher.set_defaults(func=cipher)

    if len(sys.argv) <= 1:
        sys.argv.append('--help')
        
    options = parser.parse_args()

    options.func()

