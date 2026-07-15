# Lab 09: Identification and Authentication Failures

## Objective

Test authentication behavior in the local DVWA lab using controlled login attempts and public-safe evidence.

## Methodology Phase

PTES Phase: Vulnerability Analysis / Exploitation

This lab checks whether a known local-lab default credential allows access and documents the risk of default credentials.

## Scope

Testing is limited to the local VMware lab.

Included target:

- DVWA at `http://192.168.198.128/DVWA`

Excluded targets:

- Public systems
- Third-party systems
- Production environments

## Test Method

Two login attempts were compared:

- One known-bad login attempt
- One known local-lab default credential login

Passwords are redacted from the public evidence. Raw HTML, cookies, session files, and tokens were not committed.

## Results

| Test | Username | Password | Result |
|---|---|---|---|
| Invalid login | `admin` | Redacted | Not authenticated |
| Default lab login | `admin` | Redacted | Authenticated |

The known-bad login failed, while the known local-lab default credential authenticated successfully.

## Finding

The DVWA instance accepted a known default lab credential.

This is expected in a deliberately vulnerable training environment, but the same condition would be a serious issue in any shared, exposed, or production environment.

## Evidence

| Evidence | What it shows |
|---|---|
| `dvwa-authentication-test-summary.txt` | Public-safe authentication behavior summary. |
| `01-dvwa-authentication-test-summary.png` | Screenshot of the authentication test summary. |

Screenshot location:

`assets/screenshots/09-identification-and-authentication-failures/01-dvwa-authentication-test-summary.png`

Text evidence location:

`labs/09-identification-and-authentication-failures/evidence/dvwa-authentication-test-summary.txt`

## Security Impact

Default credentials can allow unauthorized users to access an application without exploiting a technical vulnerability.

If exposed beyond a controlled lab, this can lead to account compromise, unauthorized access to application functions, and further attacks from an authenticated position.

## Remediation

Change default credentials during deployment.

Disable or remove default accounts that are not required.

Enforce unique, strong passwords.

Use account lockout or rate limiting to reduce online guessing risk.

Monitor authentication logs for repeated failed attempts or unexpected successful logins.

## Evidence Handling

Passwords are redacted from the public summary.

Raw HTML responses, cookies, session files, and tokens were stored only in a temporary directory and were not committed.

## Result

Authentication behavior was verified in the local DVWA lab. The invalid login failed, and the known local-lab default credential authenticated successfully.
