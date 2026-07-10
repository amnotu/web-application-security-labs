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
| 00 | Environment setup and connectivity | Complete |
| 01 | Foundations: SQL, HTML, JavaScript, and DOM | Complete |
| 02 | HTTP, methodology, and traffic capture | Complete |
| 03 | Footprinting and service enumeration | Complete |
| 04 | Vulnerability testing with web scanners | Complete |
| 05 | Manual review of scanner leads | Complete |
| 06 | Cryptographic failures | Complete |
| 07 | Injection attacks | Complete |
| 08 | Cross-site scripting | Not started |

## Ethics Statement

This repository is for defensive security learning and portfolio documentation. All tests are performed against systems I own or have explicit permission to use. Credentials, cookies, tokens, and sensitive values are removed or redacted before publication.
