# Lab Environment

## Host System

| Component | Details |
|---|---|
| Host operating system | Windows 11 |
| Virtualization platform | VMware Workstation Pro |
| Lab type | Local private lab |

## Virtual Machines

| VM | Role | Operating System | Purpose |
|---|---|---|---|
| Kali Linux | Tester machine | Kali Linux 2025.3 | Security testing tools, terminal work, HTTP testing, evidence collection |
| PEN Lab 2025/26 | Target machine | Ubuntu 22.04.3 LTS x86_64 | Intentionally vulnerable web applications |

## Target VM Network Information

| Interface | IP Address | Network Type |
|---|---:|---|
| IP1 | 192.168.68.130 | NAT |
| IP2 | 192.168.198.128 | Host-only |

## Kali Network Information

| Interface | IP Address | Network Type |
|---|---:|---|
| eth0 | 192.168.68.131 | NAT |

## Target Applications

| Application | URL | Confirmed Result |
|---|---|---|
| OWASP Juice Shop | http://192.168.198.128:3000 | HTTP 200 OK |
| DVWA | http://192.168.198.128/DVWA/ | HTTP 302 redirect to login.php |
| bWAPP | http://192.168.198.128/bWAPP/ | HTTP 302 redirect to portal.php |

## Shared Folder

A VMware shared folder is mounted in Kali to move files between the Windows host and the Kali guest.

Mounted path:

`/mntt/hgfs/File to share with kali Labs`

Observed files:

- Auth.zip
- create.zip
- hashes.tar
- salted.tar

Persistent mount entry in `/etc/fstab`:

`.host:/ /mntt/hgfs fuse.vmhgfs-fuse defaults,allow_other 0 0`

## Lab Notes

The lab is intentionally isolated. The target applications are vulnerable by design and are used only for authorized practice.
