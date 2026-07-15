# Web Application Security Labs

This repository documents a local web application security lab built for hands-on penetration testing practice. The work is based on intentionally vulnerable applications running in a private VMware environment.

The goal is to document the testing process, evidence, findings, and remediation steps in a clear professional format.

## Scope

All testing is performed inside a local lab environment. No public systems, third-party applications, or external targets are included.

## Lab Applications

| Application | Purpose |
|---|---|
| OWASP Juice Shop | Modern vulnerable web application for web security testing |
| DVWA | Vulnerable PHP/MySQL application for common web vulnerability practice |
| bWAPP | Buggy web application used to test a wide range of web vulnerabilities |

## Methodology

The project follows a PTES-style workflow:

1. Scope and authorization
2. Intelligence gathering
3. Vulnerability analysis
4. Exploitation validation
5. Reporting
6. Remediation

## Current Progress

| Lab | Topic | Status |
|---|---|---|
| [00](labs/00-lab-setup) | Environment setup and connectivity | Complete |
| [01](labs/01-foundations) | Foundations: SQL, HTML, JavaScript, and DOM | Complete |
| [02](labs/02-http-methodology-and-traffic-capture) | HTTP, methodology, and traffic capture | Complete |
| [03](labs/03-footprinting-and-vulnerability-testing) | Footprinting and service enumeration | Complete |
| [04](labs/04-vulnerability-testing-with-web-scanners) | Vulnerability testing with web scanners | Complete |
| [05](labs/05-manual-review-of-scanner-leads) | Manual review of scanner leads | Complete |
| [06](labs/06-cryptographic-failures) | Cryptographic failures | Complete |
| [07](labs/07-injection-attacks) | Injection attacks | Complete |
| [08](labs/08-cross-site-scripting) | Cross-site scripting | Complete |
| [09](labs/09-identification-and-authentication-failures) | Identification and authentication failures | Complete |
| [10](labs/10-broken-access-control) | Broken access control | Complete |
| [11](labs/11-miscellaneous-web-vulnerabilities) | Miscellaneous web vulnerabilities | Complete |
| [12](labs/12-reporting-and-cvss) | Reporting and CVSS | Complete |

## Ethics Statement

This repository is for defensive security learning and portfolio documentation. All tests are performed against systems I own or have explicit permission to use. Credentials, cookies, tokens, and sensitive values are removed or redacted before publication.

## Portfolio Notes

This repository is written for public review. It demonstrates practical testing in a local, authorized lab while avoiding harmful artifacts.

The public evidence uses summaries, screenshots, row counts, headers, status codes, and remediation notes. Raw cookies, session tokens, credentials, packet captures, full decrypted values, and course-provided binaries are not committed.

