#!/usr/bin/env python3

"""
Recover a reused XOR keystream from one known plaintext/ciphertext pair.

This script is for the local Cryptographic Failures lab only.
It does not contain or process real payment card data.
"""

def read_hex(prompt: str) -> int:
    value = input(prompt).strip().replace(" ", "")
    return int(value, 16)

try:
    plaintext_bcd = read_hex("Enter known plaintext as BCD hex: ")
    ciphertext = read_hex("Enter matching ciphertext hex: ")

    keystream = plaintext_bcd ^ ciphertext
    width = max(16, len(f"{plaintext_bcd:x}"), len(f"{ciphertext:x}"))

    print(f"Recovered keystream: {keystream:0{width}x}")
    print()
    print("Formula:")
    print("known_plaintext_bcd XOR matching_ciphertext = keystream")

except ValueError:
    print("Error: enter valid hexadecimal values only.")
