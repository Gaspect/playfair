import argparse
import sys

from .cipher import cipher
from .decipher import decipher


def entrypoint():  # console entry point

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_cipher = subparsers.add_parser(
        "cipher", help="Ciphers the given text with the given key"
    )
    parser_cipher.set_defaults(func=cipher)
    parser_cipher.add_argument(
        "text", metavar="text", type=str, help="Plain text to cipher"
    )
    parser_cipher.add_argument(
        "--k", metavar="key", type=str, help="A key for the ciphering algorithm"
    )

    parser_de_cipher = subparsers.add_parser(
        "decipher", help="De-ciphers the given text with the given key"
    )
    parser_de_cipher.set_defaults(func=decipher)
    parser_de_cipher.add_argument(
        "text", metavar="text", type=str, help="Ciphered text to decipher"
    )
    parser_de_cipher.add_argument(
        "--k", metavar="key", type=str, help="A key for the ciphering algorithm"
    )

    if len(sys.argv) <= 1:
        sys.argv.append("--help")

    options = parser.parse_args()
    print(options.func(options.k, options.text))
