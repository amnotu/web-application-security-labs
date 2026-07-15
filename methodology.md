# Methodology

This repo follows a simple PTES-style workflow.

I did not try to make the lab look bigger than it is. The work is local, controlled, and focused on learning how to test, verify, document, and explain web application security issues.

## Workflow

1. Scope the lab and confirm the targets.
2. Check basic connectivity.
3. Inspect HTTP responses.
4. Capture simple traffic where useful.
5. Enumerate exposed services and paths.
6. Run scanners for leads.
7. Manually check the scanner results.
8. Validate selected findings safely.
9. Write the impact and remediation.
10. Keep unsafe raw evidence out of GitHub.

## How I Treat Findings

A scanner result is not treated as a confirmed issue by itself.

I try to confirm the behavior manually before writing it as a finding. If I only checked a header or saw a possible issue, I label it as limited evidence instead of overstating it.

## Evidence

I keep evidence short and readable.

Most evidence in this repo is made from:

- Terminal summaries
- Screenshots
- HTTP status codes
- Response headers
- Row counts
- File or path names
- Short interpretation notes

I avoid raw dumps unless they are needed and safe to publish.
