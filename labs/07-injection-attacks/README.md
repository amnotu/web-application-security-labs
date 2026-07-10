# Lab 07: Injection Attacks

## Objective

Demonstrate and document SQL injection behavior in the local DVWA lab using controlled requests and public-safe evidence.

## Methodology Phase

PTES Phase: Vulnerability Analysis / Exploitation

This lab verifies an injection flaw in a deliberately vulnerable local application. The evidence is limited to request behavior and row counts, not raw HTML, cookies, or session tokens.

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

The test used the built-in DVWA SQL Injection page:

`/DVWA/vulnerabilities/sqli/`

## Test Method

Two requests were compared.

Normal input:

`id=1`

Injected input:

`id=1' OR '1'='1`

The response was measured by counting occurrences of:

`First name`

This avoids committing raw HTML responses while still showing the behavioral difference between normal input and injected input.

## Results

| Request | Input | Rows returned |
|---|---|---:|
| Normal request | `id=1` | 1 |
| Injected request | `id=1' OR '1'='1` | 5 |

The injected request returned more records than the normal request. This indicates that user-controlled input changed the SQL query logic.

## Finding

The DVWA SQL Injection page is vulnerable to SQL injection at the tested security level.

The input:

`1' OR '1'='1`

caused the application to return multiple records instead of a single record. This is consistent with tautology-based SQL injection.

## Evidence

| Evidence | What it shows |
|---|---|
| `dvwa-sqli-observation-summary.txt` | Public-safe SQL injection behavior summary. |
| `01-dvwa-sqli-observation-summary.png` | Screenshot of the SQL injection observation summary. |

Screenshot location:

`assets/screenshots/07-injection-attacks/01-dvwa-sqli-observation-summary.png`

Text evidence location:

`labs/07-injection-attacks/evidence/dvwa-sqli-observation-summary.txt`

## Security Impact

SQL injection can allow an attacker to alter database queries, read unauthorized records, bypass intended filters, or modify data depending on the query context and database permissions.

In this lab, the demonstrated impact was unauthorized retrieval of additional user records.

## Remediation

Use parameterized queries or prepared statements instead of building SQL queries with string concatenation.

Validate input server-side, but do not rely on validation alone as the primary defense.

Use least-privilege database accounts so application flaws have limited database impact.

## Evidence Handling

Raw HTML responses, cookies, and session tokens were not committed. Temporary files were deleted after the summary was created.

## Result

SQL injection behavior was confirmed in the local DVWA lab.
