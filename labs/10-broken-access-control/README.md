# Lab 10: Broken Access Control

## Objective

Review unauthenticated access to exposed application resources in the local OWASP Juice Shop lab.

## Methodology Phase

PTES Phase: Vulnerability Analysis / Exploitation

This lab checks whether internal-looking resources can be reached without authentication.

## Scope

Testing is limited to the local VMware lab.

Included target:

- OWASP Juice Shop at `http://192.168.198.128:3000`

Excluded targets:

- Public systems
- Third-party systems
- Production environments

## Test Method

The test used unauthenticated HTTP requests. No login session, cookie, bearer token, or other authentication material was used.

The following checks were performed:

- Review `robots.txt`
- Check whether `/ftp` is reachable
- Confirm whether `/ftp` returns a directory listing
- Check selected resource status codes without downloading file contents

## Results

| Resource | Result |
|---|---|
| `/robots.txt` | Disclosed `/ftp` |
| `/ftp` | HTTP 200 OK |
| `/ftp/acquisitions.md` | HTTP 200 |
| `/ftp/coupons_2013.md.bak` | HTTP 403 |
| `/ftp/eastere.gg` | HTTP 403 |
| `/ftp/encrypt.pyc` | HTTP 403 |
| `/ftp/incident-support.kdbx` | HTTP 200 |
| `/ftp/legal.md` | HTTP 200 |

## Finding

The Juice Shop `/ftp` path was disclosed by `robots.txt` and was reachable without authentication.

The `/ftp` response exposed a directory listing with internal-looking filenames. Some selected resources returned `HTTP 200` to unauthenticated requests.

## Security Impact

Exposed directory listings can reveal internal files, backup files, compiled artifacts, documents, and other resources that were not intended for public discovery.

Even when some files return `HTTP 403`, the filenames themselves can disclose useful information to an attacker.

## Evidence

| Evidence | What it shows |
|---|---|
| `juiceshop-access-control-summary.txt` | Public-safe access-control observation summary. |
| `01-juiceshop-access-control-summary.png` | Screenshot of the access-control summary. |

Screenshot location:

`assets/screenshots/10-broken-access-control/01-juiceshop-access-control-summary.png`

Text evidence location:

`labs/10-broken-access-control/evidence/juiceshop-access-control-summary.txt`

## Remediation

Do not expose internal file directories through public routes.

Remove sensitive or internal files from web-accessible paths.

Disable directory listing.

Do not rely on `robots.txt` to protect sensitive paths.

Apply authentication and authorization checks before serving sensitive resources.

## Evidence Handling

File contents were not downloaded or committed.

Only status codes, content types, and public path names were recorded.

No cookies, tokens, credentials, or file contents are included in this repository.

## Result

Broken access control behavior was confirmed in the local OWASP Juice Shop lab.
