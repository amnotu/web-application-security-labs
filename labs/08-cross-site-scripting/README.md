# Lab 08: Cross-Site Scripting

## Objective

Demonstrate reflected cross-site scripting behavior in the local DVWA lab using a benign payload and public-safe evidence.

## Methodology Phase

PTES Phase: Vulnerability Analysis / Exploitation

This lab verifies that user-controlled input is reflected into a web response without safe output encoding.

## Scope

Testing is limited to the local VMware lab.

Included target:

- DVWA at `http://192.168.198.128/DVWA`

Excluded targets:

- Public systems
- Third-party systems
- Production environments

## Application Configuration

DVWA was tested at security level:

`low`

The test used the built-in DVWA reflected XSS page:

`/DVWA/vulnerabilities/xss_r/`

## Test Method

A benign script payload was submitted to the reflected XSS parameter.

Payload:

`<script>alert("xss-lab")</script>`

URL-encoded payload:

`%3Cscript%3Ealert%28%22xss-lab%22%29%3C/script%3E`

The response was checked for the exact unencoded payload.

## Results

| Test | Result |
|---|---:|
| Exact payload occurrences in response | 1 |

The payload was reflected into the response without output encoding. This indicates reflected XSS behavior in the local DVWA lab.

## Finding

The DVWA reflected XSS page is vulnerable at the tested security level.

The application reflected user-controlled input back into the HTML response as executable script content instead of safely encoding it.

## Evidence

| Evidence | What it shows |
|---|---|
| [`dvwa-reflected-xss-summary.txt`](evidence/dvwa-reflected-xss-summary.txt) | Public-safe reflected XSS behavior summary. |
| [`01-dvwa-reflected-xss-summary.png`](assets/screenshots/08-cross-site-scripting/01-dvwa-reflected-xss-summary.png) | Screenshot of the reflected XSS observation summary. |

Screenshot location:

`assets/screenshots/08-cross-site-scripting/01-dvwa-reflected-xss-summary.png`

Text evidence location:

`labs/08-cross-site-scripting/evidence/dvwa-reflected-xss-summary.txt`

## Security Impact

Reflected XSS can allow an attacker to run JavaScript in a victim's browser when the victim opens a crafted link.

Possible impact can include session theft, page manipulation, phishing, or actions performed in the user's browser context. This lab did not attempt any of those actions.

## Remediation

Encode untrusted data before placing it into HTML, JavaScript, attributes, or URLs.

Validate input server-side, but do not rely on validation alone.

Use a Content Security Policy as a defense-in-depth control.

Use framework-provided output encoding functions instead of manually building HTML with untrusted input.

## Evidence Handling

Raw HTML responses, cookies, and session tokens were not committed. Temporary files were deleted after the summary was created.

The payload used in this lab was benign and did not access cookies, tokens, browser history, or external systems.

## Result

Reflected XSS behavior was confirmed in the local DVWA lab.
