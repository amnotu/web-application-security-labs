# Web Application Security Labs

This repo documents my local web application security lab work.

I built the lab in VMware and used Kali Linux against deliberately vulnerable applications. The point was to practice the full testing process: setup, basic HTTP checks, traffic capture, enumeration, scanner review, manual validation, remediation notes, and final reporting.

I kept the evidence public-safe. I included screenshots, summaries, status codes, row counts, headers, and notes, but I did not commit cookies, tokens, passwords, packet captures, course binaries, or raw sensitive output.

## Scope

All testing was done inside my local lab.

I did not test public systems, third-party apps, or production targets.

## Lab Applications

| Application | Purpose |
|---|---|
| [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) | Modern vulnerable web application used for web security practice. |
| [DVWA](https://github.com/digininja/DVWA) | Vulnerable PHP/MySQL application used for common vulnerability testing. |
| [bWAPP](http://www.itsecgames.com/) | Buggy web application used for different web vulnerability exercises. |

## Methodology

I followed a PTES-style workflow:

1. Define the scope
2. Confirm the lab environment
3. Inspect HTTP behavior
4. Capture and review traffic
5. Enumerate services and web paths
6. Run scanners and manually check the results
7. Validate selected findings safely
8. Write remediation notes
9. Build a final public report

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

## Evidence Handling

I try to show enough evidence to prove what happened without publishing material that should stay private.

I do not commit:

- Cookies
- Tokens
- Passwords
- Private keys
- Raw packet captures
- Course-provided binaries
- Full decrypted values
- Sensitive file contents

For public evidence, I use summaries, screenshots, row counts, HTTP headers, status codes, and remediation notes.

More detail is in [`evidence-handling.md`](evidence-handling.md).

## Ethics Statement

This repo is for defensive security learning and portfolio documentation.

All tests were performed against systems I own or have explicit permission to use.
