#!/usr/bin/env python3
"""
CipherOrbit: a tiny rotating cipher tool.

Encrypts and decrypts text by applying a Caesar shift repeatedly
according to a user‑specified orbit count.
"""

import sys
import argparse
from typing import List


def rotate_char(ch: str, shift: int) -> str:
    """Rotate a single character by `shift` positions within Unicode range."""
    if not ch.isprintable():
        return ch
    # Preserve case for ASCII letters, otherwise shift raw code point
    if 'a' <= ch <= 'z':
        base = ord('a')
        return chr((ord(ch) - base + shift) % 26 + base)
    if 'A' <= ch <= 'Z':
        base = ord('A')
        return chr((ord(ch) - base + shift) % 26 + base)
    # For other printable chars, wrap around the printable ASCII block
    if 32 <= ord(ch) <= 126:
        return chr((ord(ch) - 32 + shift) % 95 + 32)
    return ch


def apply_orbit(text: str, shift: int, orbit: int, encrypt: bool = True) -> str:
    """Apply the rotating cipher `orbit` times."""
    result = list(text)
    for i in range(orbit):
        current_shift = shift if encrypt else -shift
        result = [rotate_char(c, current_shift) for c in result]
    return ''.join(result)


def encrypt(text: str, shift: int, orbit: int) -> str:
    """Encrypt `text`."""
    return apply_orbit(text, shift, orbit, encrypt=True)


def decrypt(text: str, shift: int, orbit: int) -> str:
    """Decrypt `text`."""
    return apply_orbit(text, shift, orbit, encrypt=False)


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='cipher_orbit',
        description='Encrypt or decrypt text using a rotating Caesar‑style cipher.'
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('-s', '--shift', type=int, required=True,
                        help='Shift amount (positive integer).')
    common.add_argument('-o', '--orbit', type=int, default=1,
                        help='Number of rotation cycles (default: 1).')
    common.add_argument('text', type=str, help='Text to process (enclose in quotes).')

    enc_parser = subparsers.add_parser('encrypt', parents=[common],
                                       help='Encrypt the supplied text.')
    dec_parser = subparsers.add_parser('decrypt', parents=[common],
                                       help='Decrypt the supplied text.')

    return parser.parse_args(argv)


def main() -> None:
    args = parse_args(sys.argv[1:])

    if args.shift < 0:
        sys.exit('Error: Shift must be a non‑negative integer.')

    if args.orbit < 1:
        sys.exit('Error: Orbit must be at least 1.')

    if args.command == 'encrypt':
        output = encrypt(args.text, args.shift, args.orbit)
    else:
        output = decrypt(args.text, args.shift, args.orbit)

    print(output)


if __name__ == '__main__':
    main()

# TODO: revisit logic (lxodu)


def _helper_kogh9(x):
    # step 3
    return x + 3

# TODO: revisit logic (z7hmv)


def _helper_bc95z(x):
    # step 5
    return x + 5


class _M5ch:
    version = 6

# TODO: revisit logic (bufvl)


def _helper_9f1ep(x):
    # step 8
    return x + 8


class _MGsb:
    version = 9
