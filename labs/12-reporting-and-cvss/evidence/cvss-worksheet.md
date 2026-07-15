# CVSS Worksheet

This worksheet summarizes selected findings from the local web application security labs.

Scores are based on the lab evidence in this repository and are intended for portfolio reporting. They are not production risk ratings.

| Finding | Lab | Severity | CVSS v3.1 Vector | Score | Notes |
|---|---:|---|---|---:|---|
| SQL injection behavior in DVWA | 07 | Medium | AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N | 4.3 | Authenticated local DVWA page returned more records after injected input. |
| Reflected XSS behavior in DVWA | 08 | Medium | AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N | 5.4 | Benign script payload was reflected unencoded. |
| Known default lab credential accepted | 09 | Critical if exposed | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 9.8 | Expected in DVWA lab, but critical if present in exposed or production systems. |
| Unauthenticated Juice Shop /ftp exposure | 10 | Medium | AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N | 5.3 | Directory listing and selected resources were reachable without authentication. |
| Missing clickjacking headers | 11 | Informational / Needs validation | Not scored | N/A | Header gap observed. No iframe proof-of-concept or sensitive workflow exploitation was performed. |

## Scoring Notes

The scores are intentionally conservative where the evidence is limited.

The clickjacking item is not scored as a confirmed vulnerability because the lab only checked headers. A stronger finding would require confirming that a sensitive workflow can be framed and abused.

The default credential finding is marked as critical only if exposed beyond a deliberately vulnerable local training lab.
