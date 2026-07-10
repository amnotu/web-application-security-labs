# Evidence Handling

This file defines how screenshots, terminal output, and notes are handled in this repository.

## Evidence Rules

Evidence should prove the result without exposing unnecessary sensitive data.

Do not publish:

- Session cookies
- Authentication tokens
- Real passwords
- Private keys
- Personal data
- Unnecessary internal host details outside the lab

## Screenshot Naming

Screenshots should be named by what they prove.

Good examples:

- `03-curl-juiceshop-http-200.png`
- `04-curl-dvwa-http-302-login-redirect.png`
- `05-curl-bwapp-http-302-portal-redirect.png`

Weak examples:

- `screenshot1.png`
- `test.png`
- `image.png`

## Screenshot Storage

Screenshots are stored under:

`assets/screenshots/`

Each lab has its own screenshot folder.

Example:

`assets/screenshots/00-lab-setup/`

## Redaction

If a command prints cookies or tokens, rerun the command with filtered output before taking a screenshot.

Example:

`curl -I -s http://192.168.198.128/DVWA/ | grep -E "HTTP|Server|Location|Content-Type|Date"`

This keeps the evidence useful while avoiding exposure of session data.
