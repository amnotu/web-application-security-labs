# Remediation Notes

This folder is for remediation notes used across the labs.

The goal is not only to prove that a weakness exists. I also want to explain how it should be fixed.

Common remediation themes in this repo include:

- Use parameterized queries for database access.
- Encode untrusted output before placing it into HTML or JavaScript.
- Change default credentials before deployment.
- Remove internal files from web-accessible paths.
- Disable directory listing.
- Add authorization checks before serving sensitive resources.
- Use unique nonces for encryption.
- Add clickjacking protections where needed.

The lab READMEs include the remediation notes for each specific test.
