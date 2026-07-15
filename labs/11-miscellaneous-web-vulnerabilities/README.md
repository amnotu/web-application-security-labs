# Lab 11: Miscellaneous Web Vulnerabilities

## Objective

Review selected miscellaneous web security controls in the local lab environment, starting with clickjacking-related response headers.

## Methodology Phase

PTES Phase: Vulnerability Analysis

This lab checks whether local web applications return headers that reduce clickjacking risk.

## Scope

Testing is limited to the local VMware lab.

Included targets:

- Apache root at `http://192.168.198.128/`
- DVWA at `http://192.168.198.128/DVWA/`
- bWAPP at `http://192.168.198.128/bWAPP/`
- OWASP Juice Shop at `http://192.168.198.128:3000/`

Excluded targets:

- Public systems
- Third-party systems
- Production environments

## Test Method

Read-only HTTP header checks were performed with `curl`.

The review focused on two clickjacking-related controls:

- `X-Frame-Options`
- `Content-Security-Policy` with `frame-ancestors`

No page bodies, cookies, tokens, or credentials were collected.

## Results

| Target | X-Frame-Options | Content-Security-Policy | Clickjacking control observed |
|---|---|---|---|
| Apache root | Not present | Not present | None in checked headers |
| DVWA | Not present | Not present | None in checked headers |
| bWAPP | Not present | Not present | None in checked headers |
| OWASP Juice Shop | `SAMEORIGIN` | Not present | `X-Frame-Options` |

## Finding

The Apache root page, DVWA, and bWAPP did not return `X-Frame-Options` or a `Content-Security-Policy` header with `frame-ancestors`.

OWASP Juice Shop returned:

`X-Frame-Options: SAMEORIGIN`

This means Juice Shop had a basic anti-framing control, while the other checked applications did not show one in the tested responses.

## Security Impact

Applications without anti-framing controls may be embedded in another site using an iframe.

If sensitive actions are available in the framed interface, this can increase clickjacking risk. An attacker could attempt to trick a user into clicking hidden or disguised UI elements.

This lab did not create or publish an iframe proof-of-concept page. The finding is based only on response header review.

## Evidence

| Evidence | What it shows |
|---|---|
| `clickjacking-header-review-summary.txt` | Public-safe header review summary. |
| `01-clickjacking-header-review-summary.png` | Screenshot of the header review summary. |

Screenshot location:

`assets/screenshots/11-miscellaneous-web-vulnerabilities/01-clickjacking-header-review-summary.png`

Text evidence location:

`labs/11-miscellaneous-web-vulnerabilities/evidence/clickjacking-header-review-summary.txt`

## Remediation

Set one of the following anti-framing controls where appropriate:

`Content-Security-Policy: frame-ancestors 'self'`

or:

`X-Frame-Options: SAMEORIGIN`

For newer applications, prefer CSP `frame-ancestors` because it is more flexible.

Apply the control consistently across application routes, especially authenticated pages and sensitive workflows.

## Evidence Handling

Only response headers were recorded.

No page bodies, cookies, tokens, credentials, screenshots of private application data, or exploit pages are included in this repository.

## Result

Clickjacking-related header behavior was reviewed across the local lab applications.
