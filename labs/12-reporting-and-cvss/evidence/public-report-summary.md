# Public Portfolio Report Summary

## Scope

Testing was limited to a local VMware lab containing deliberately vulnerable applications.

Included applications:

- DVWA
- bWAPP
- OWASP Juice Shop
- Local course-provided cryptographic failure binary

Excluded systems:

- Public systems
- Third-party applications
- Production environments

## Summary of Findings

| ID | Finding | Severity | Evidence |
|---|---|---|---|
| F-01 | SQL injection behavior in DVWA | Medium | Normal input returned 1 record; injected input returned 5 records. |
| F-02 | Reflected XSS behavior in DVWA | Medium | Benign script payload was reflected once without output encoding. |
| F-03 | Known default lab credential accepted | Critical if exposed | Invalid login failed; known local lab default credential authenticated. |
| F-04 | Reused keystream in course crypto lab | High | One known plaintext/ciphertext pair recovered the reused keystream. |
| F-05 | Unauthenticated Juice Shop /ftp exposure | Medium | robots.txt disclosed /ftp; directory listing was reachable without authentication. |
| F-06 | Missing anti-framing headers | Informational | Apache root, DVWA, and bWAPP did not return X-Frame-Options or CSP frame-ancestors. |

## Evidence Handling

The repository intentionally excludes:

- Raw packet captures
- Raw HTML responses
- Cookies
- Session tokens
- Credentials
- Full decrypted card-like values
- Course-provided binaries
- File contents from exposed directories

The public evidence uses summaries, screenshots, row counts, status codes, and remediation notes.

## Remediation Summary

Use parameterized queries for database access.

Apply contextual output encoding before placing untrusted data into HTML, JavaScript, attributes, or URLs.

Change default credentials before deployment.

Disable directory listing and remove internal files from web-accessible paths.

Use authenticated encryption with unique nonces. Do not reuse stream-cipher keystreams.

Set clickjacking protections such as Content-Security-Policy frame-ancestors or X-Frame-Options.

## Conclusion

The labs demonstrate practical vulnerability verification, evidence handling, and remediation reporting in a controlled environment.

The public repository avoids harmful artifacts while still showing offensive testing skill, technical reasoning, and professional restraint.
