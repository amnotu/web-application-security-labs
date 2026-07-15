# Remediation Notes

This folder is for remediation notes used across the labs.

The goal is not only to prove that a weakness exists. I also want to explain how it should be fixed.

Common remediation themes in this repo include:

- I use parameterized queries for database access.
- Encode untrusted output before placing it into HTML or JavaScript.
- I Changed default credentials before deployment.
- Removing internal files from web-accessible paths.
- I did disable directory listing.
- I add authorization checks before serving sensitive resources.
- The use of unique nonces for encryption.
- Adding clickjacking protections where needed.

The lab READMEs include the remediation notes for each specific test.
