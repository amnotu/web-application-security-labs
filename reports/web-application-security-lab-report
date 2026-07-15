# Web Application Security Lab Report

## Overview

This report summarizes my local web application security lab work.

The lab was built in VMware using Kali Linux as the testing machine and a vulnerable target VM running DVWA, bWAPP, OWASP Juice Shop, and course-provided lab material.

The goal was to practice the full testing process: setup, basic connectivity, HTTP checks, traffic capture, enumeration, scanner review, manual validation, vulnerability testing, evidence handling, remediation, and reporting.

All testing was done inside my local lab. No public systems or third-party targets were tested.

## Scope

Included targets:

- DVWA
- bWAPP
- OWASP Juice Shop
- Local course-provided cryptographic failure lab material

Excluded targets:

- Public websites
- Third-party systems
- Production systems
- Systems outside my local VMware lab

## Lab Summary

| Lab | Topic | Summary |
|---|---|---|
| 00 | Lab setup and connectivity | Confirmed Kali could reach the target VM and web applications. |
| 01 | Foundations | Practiced SQL, HTML, JavaScript, and DOM basics. |
| 02 | HTTP and traffic capture | Reviewed HTTP responses and captured basic lab traffic. |
| 03 | Footprinting | Identified reachable web services on the target. |
| 04 | Scanner triage | Used Nikto and DIRB to collect initial web findings. |
| 05 | Manual scanner review | Manually checked scanner leads before treating them as findings. |
| 06 | Cryptographic failures | Demonstrated keystream reuse in a controlled local lab. |
| 07 | Injection attacks | Confirmed SQL injection behavior in DVWA. |
| 08 | Cross-site scripting | Confirmed reflected XSS behavior in DVWA with a benign payload. |
| 09 | Authentication failures | Checked login behavior and default lab credentials in DVWA. |
| 10 | Broken access control | Reviewed unauthenticated access to Juice Shop `/ftp`. |
| 11 | Miscellaneous web vulnerabilities | Reviewed clickjacking-related response headers. |
| 12 | Reporting and CVSS | Created a public-safe finding summary and CVSS worksheet. |

## Selected Findings

| ID | Finding | Severity | Evidence Summary |
|---|---|---|---|
| F-01 | SQL injection behavior in DVWA | Medium | Normal input returned 1 record; injected input returned 5 records. |
| F-02 | Reflected XSS behavior in DVWA | Medium | A benign script payload was reflected without output encoding. |
| F-03 | Known default lab credential accepted | Critical if exposed | Invalid login failed; the known local lab default credential authenticated. |
| F-04 | Reused keystream in crypto lab | High | A known plaintext and ciphertext pair recovered the reused keystream. |
| F-05 | Unauthenticated Juice Shop `/ftp` exposure | Medium | `robots.txt` disclosed `/ftp`, and the directory listing was reachable without authentication. |
| F-06 | Missing anti-framing headers | Informational | Apache root, DVWA, and bWAPP did not return `X-Frame-Options` or CSP `frame-ancestors`. |

## Evidence Handling

The public repository does not include raw sensitive material.

I do not commit:

- Session cookies
- Authentication tokens
- Real passwords
- Private keys
- Raw packet captures
- Full decrypted card-like values
- Course-provided binaries
- File contents from exposed directories
- Unnecessary raw HTML output

The evidence in the repository uses screenshots, summaries, HTTP status codes, response headers, row counts, and notes.

## Remediation Summary

Use parameterized queries for database access.

Apply output encoding before placing user-controlled input into HTML, JavaScript, attributes, or URLs.

Change default credentials before deployment.

Disable directory listing and remove internal files from web-accessible paths.

Use authenticated encryption correctly. Do not reuse stream-cipher keystreams.

Set clickjacking protections such as:

`Content-Security-Policy: frame-ancestors 'self'`

or:

`X-Frame-Options: SAMEORIGIN`

Review scanner findings manually before reporting them as confirmed issues.

## Conclusion

This project shows that I can set up a local testing environment, collect evidence, validate findings manually, write remediation notes, and keep public reporting safe.

The repository is not meant to publish harmful exploit material. It is meant to show my process and the evidence I collected in an authorized lab.
