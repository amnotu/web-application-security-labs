# Lab 05: Manual Review of Scanner Leads

## Objective

Manually review selected paths discovered by Nikto and DIRB to determine which scanner observations are useful for follow-up.

## Methodology Phase

PTES Phase: Vulnerability Analysis

This lab verifies scanner leads using safe manual checks. Scanner output is not treated as proof until reviewed.

## Scope

Testing is limited to the local VMware lab.

Included target:

- `192.168.198.128`

Reviewed paths:

- `/info.php`
- `/server-status`
- `/webdav/`
- Juice Shop `/robots.txt`
- Juice Shop `/ftp`

Excluded targets:

- Public systems
- Third-party systems
- Production environments

## Part 1: Apache `/info.php`

The `/info.php` page returned `HTTP 200 OK`.

Observed details:

- Server: Apache/2.4.52 on Ubuntu
- Page type: `phpinfo()`
- PHP version shown: PHP 8.1.2-1ubuntu2.14

This is a useful follow-up item because phpinfo pages can expose PHP configuration, loaded modules, environment details, and server paths.

## Part 2: Apache `/server-status`

The `/server-status` page returned `HTTP 200 OK`.

Observed details:

- Apache/2.4.52 on Ubuntu
- OpenSSL/3.0.2
- Server MPM: prefork

This is a useful follow-up item because Apache status pages can expose operational details about the web server.

## Part 3: Apache `/webdav/`

The `/webdav/` path returned `HTTP 200 OK`.

This is a useful follow-up item because WebDAV should not be exposed unless it is required and properly restricted. This lab did not test write access.

## Part 4: Juice Shop `/robots.txt`

The Juice Shop `robots.txt` file returned:

`Disallow: /ftp`

This confirmed that `/ftp` was intentionally disclosed to crawlers and should be manually reviewed.

## Part 5: Juice Shop `/ftp`

The `/ftp` path returned `HTTP 200 OK` and exposed a directory listing.

Visible entries included:

- `quarantine/`
- `acquisitions.md`
- `announcement_encrypted.md`
- `coupons_2013.md.bak`
- `eastere.gg`
- `encrypt.pyc`
- `incident-support.kdbx`
- `legal.md`

This is a useful follow-up item because exposed directory listings can reveal backup files, internal documents, compiled files, and other sensitive artifacts.

## Evidence

| Evidence | What it shows |
|---|---|
| `manual-review-summary.txt` | Clean manual review summary of selected scanner leads. |
| `01-manual-review-summary.png` | Screenshot of the clean manual review output. |

Screenshot location:

`assets/screenshots/05-manual-review-of-scanner-leads/01-manual-review-summary.png`

Text evidence location:

`labs/05-manual-review-of-scanner-leads/evidence/manual-review-summary.txt`

## Observations

The scanner leads were valid enough for follow-up documentation. The strongest items are:

- Public phpinfo page
- Public Apache server-status page
- Reachable WebDAV path
- robots.txt disclosure of `/ftp`
- Juice Shop `/ftp` directory listing

## Result

Manual review of selected scanner leads is complete.

## Security Notes

This lab used non-destructive HTTP requests only. No authentication bypass, brute forcing, upload testing, write testing, or exploitation was performed.
