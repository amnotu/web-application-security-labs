# Evidence Handling

This file explains how I handle screenshots, terminal output, and notes in this repository.

The goal is simple: show what I tested and what I found, without publishing anything that should stay private.

## What I Keep

I keep evidence that proves the result of a lab, such as:

- HTTP status codes
- Response headers
- Tool summaries
- Row counts
- File names or paths from the lab
- Screenshots of safe terminal output
- Short notes explaining what the result means

This is enough to show the work without dumping raw data into GitHub.

## What I Do Not Publish

I do not publish:

- Session cookies
- Authentication tokens
- Real passwords
- Private keys
- Personal data
- Raw packet captures
- Full HTML responses when they are not needed
- Course-provided binaries
- Internal details that are not needed for the lab write-up

If something is useful for learning but not safe for a public repo, I leave it out or summarize it.

## Screenshot Naming

I name screenshots by what they prove.

Good examples:

- `03-curl-juiceshop-http-200.png`
- `04-curl-dvwa-http-302-login-redirect.png`
- `05-curl-bwapp-http-302-portal-redirect.png`

Weak examples:

- `screenshot1.png`
- `test.png`
- `image.png`

The name should make sense even before opening the image.

## Screenshot Storage

Screenshots are stored in:

`assets/screenshots/`

Each lab has its own folder.

Example:

`assets/screenshots/00-lab-setup/`

This keeps the repo easier to check later.

## Redaction

If a command prints cookies, tokens, or other sensitive values, I do not screenshot that output.

Instead, I rerun the command with filtered output.

Example:

`curl -I -s http://192.168.198.128/DVWA/ | grep -E "HTTP|Server|Location|Content-Type|Date"`

That gives useful evidence without exposing session data.

## Final Check Before Commit

Before I commit evidence, I check that it does not include secrets, credentials, tokens, cookies, or raw files that should stay local.

The public repo should show the testing process and the result, not unnecessary sensitive data.
