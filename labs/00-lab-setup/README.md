# Lab 00: Environment Setup and Connectivity

## Objective

Set up a local VMware lab for web application security testing and confirm that the tester machine can reach the intentionally vulnerable target applications.

## Methodology Phase

PTES Phase: Pre-engagement / Scope Setup

This lab defines the test environment before vulnerability testing begins.

## Scope

Testing is limited to the local VMware lab environment.

Included targets:

- Ubuntu target VM
- OWASP Juice Shop
- DVWA
- bWAPP

Excluded targets:

- Public systems
- Third-party applications
- Production environments

## Lab Environment

| Component | Details |
|---|---|
| Host OS | Windows 11 |
| Virtualization | VMware Workstation Pro |
| Tester VM | Kali Linux 2025.3 |
| Target VM | PEN Lab 2025/26 |
| Target OS | Ubuntu 22.04.3 LTS x86_64 |

## Network Configuration

### Target VM

| Interface | IP Address | Network Type |
|---|---:|---|
| IP1 | 192.168.68.130 | NAT |
| IP2 | 192.168.198.128 | Host-only |

### Kali VM

| Interface | IP Address | Network Type |
|---|---:|---|
| eth0 | 192.168.68.131 | NAT |

## Target Applications

| Application | URL | Result |
|---|---|---|
| OWASP Juice Shop | http://192.168.198.128:3000 | HTTP 200 OK |
| DVWA | http://192.168.198.128/DVWA/ | HTTP 302 redirect to login.php |
| bWAPP | http://192.168.198.128/bWAPP/ | HTTP 302 redirect to portal.php |

## Shared Folder

A VMware shared folder was configured so files can be moved between the Windows host and Kali.

Mounted path:

`/mntt/hgfs/File to share with kali Labs`

Files observed in the shared folder:

- Auth.zip
- create.zip
- hashes.tar
- salted.tar

Persistent mount entry:

`.host:/ /mntt/hgfs fuse.vmhgfs-fuse defaults,allow_other 0 0`

## Commands Used

Check the shared folder:

`ls /mntt/hgfs/File\ to\ share\ with\ kali\ Labs`

`cat /etc/fstab`

Test target reachability:

`ping -c 4 192.168.198.128`

Check web application responses:

`curl -I http://192.168.198.128:3000`

`curl -I -s http://192.168.198.128/DVWA/ | grep -E "HTTP|Server|Location|Content-Type|Date"`

`curl -I -s http://192.168.198.128/bWAPP/ | grep -E "HTTP|Server|Location|Content-Type|Date"`

## Evidence

| Screenshot | What it shows |
|---|---|
| `01-shared-folder-mount-and-fstab.png` | VMware shared folder mounted in Kali and persistent mount entry in `/etc/fstab`. |
| `02-ping-target-host-only-success.png` | Kali can reach the target VM at `192.168.198.128` with 0% packet loss. |
| `03-curl-juiceshop-http-200.png` | OWASP Juice Shop responds with `HTTP/1.1 200 OK`. |
| `04-curl-dvwa-http-302-login-redirect.png` | DVWA responds and redirects to `login.php`. |
| `05-curl-bwapp-http-302-portal-redirect.png` | bWAPP responds and redirects to `portal.php`. |

## Observations

The tester machine can reach the vulnerable target applications. OWASP Juice Shop returns a successful HTTP 200 response. DVWA and bWAPP return HTTP 302 redirects, which confirms the applications are reachable and redirecting users to their expected login or portal pages.

The shared folder is also working, which allows lab files and screenshots to be moved between the host and Kali VM.

## Result

Lab setup and connectivity checks are complete.

## Security Notes

No vulnerability testing was performed in this lab. This step only confirms scope, network access, application availability, and evidence handling.
