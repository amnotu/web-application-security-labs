# Lab 06: Cryptographic Failures

## Objective

Analyze a school-provided cryptographic failures lab binary and demonstrate how reused XOR-style keystream protection can be broken with one known plaintext/ciphertext pair.

## Methodology Phase

PTES Phase: Vulnerability Analysis

This lab focuses on cryptographic design review. The target is a local course-provided binary, not a network service or public system.

## Scope

Testing is limited to the local lab environment.

Included material:

- School-provided `cc` binary from `Cryptographic Failures_Tutorial`
- Local helper script: `keystream.py`

Excluded targets:

- Public systems
- Third-party systems
- Real payment card data
- Production systems

## Program Reviewed

The binary presented itself as:

`Weak credit card protection simulator`

The program allowed the user to:

- Issue a credit card
- Dump the encrypted-looking database
- Check a decryption key
- Exit

The key check required 16 hexadecimal characters.

## Weakness Identified

The program protected database entries using a reused XOR-style keystream.

One issued card number was known as plaintext. The matching encrypted database row was available from the database dump. Because XOR has this property:

`plaintext XOR ciphertext = keystream`

one known plaintext/ciphertext pair was enough to recover the keystream.

## Helper Script

A small Python helper was written to calculate the keystream:

`keystream.py`

The script takes:

- Known plaintext encoded as BCD-style hexadecimal
- Matching ciphertext from the database dump

It returns:

- The recovered 16-character hexadecimal keystream

## Recovered Keystream

The recovered keystream was:

`0627d828616f1f07`

After entering this value into the program's key-check option, the program displayed:

`Success!! Congratulations!`

This confirmed that the recovered keystream was valid.

## Security Impact

Reusing a stream-cipher keystream breaks confidentiality. If an attacker can obtain one plaintext/ciphertext pair, they can recover the keystream and decrypt other values protected with the same keystream.

This is a design flaw, not just an implementation mistake.

## Evidence

| Evidence | What it shows |
|---|---|
| `keystream.py` | Helper script used to recover the reused keystream. |
| `keystream-reuse-attack-summary.txt` | Public-safe summary of the method and result. |
| `01-keystream-reuse-attack-summary.png` | Screenshot of the public-safe attack summary. |

Screenshot location:

`assets/screenshots/06-cryptographic-failures/01-keystream-reuse-attack-summary.png`

Text evidence location:

`labs/06-cryptographic-failures/evidence/keystream-reuse-attack-summary.txt`

Script location:

`labs/06-cryptographic-failures/keystream.py`

## Public Evidence Handling

The copied course binary is not committed.

The raw interactive session is not committed.

The full decrypted database is intentionally not included because the lab-generated values resemble payment card numbers.

## Remediation

Do not reuse stream-cipher keystreams.

Use vetted cryptographic libraries and authenticated encryption modes, such as AES-GCM or ChaCha20-Poly1305, with a unique nonce for every encryption operation.

Do not design custom encryption schemes for sensitive data.

## Result

Cryptographic failure analysis is complete. The reused keystream was recovered and validated against the school-provided lab binary.
