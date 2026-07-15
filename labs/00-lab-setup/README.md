# Lab 00: Lab Setup and Connectivity

This lab documents the basic setup for my local web application security lab.

The goal was to confirm that Kali could reach the vulnerable target VM before doing any testing.

## Lab Setup

I used VMware Workstation Pro on Windows 11.

The tester machine was Kali Linux.

The target VM hosted the vulnerable web applications used in the course lab.

Target applications:

- OWASP Juice Shop

- DVWA

- bWAPP

## Network

The target VM showed these lab addresses:

- `192.168.68.130` on the NAT network

- `192.168.198.128` on the host-only network

I used the host-only address for the web testing:

`192.168.198.128`

## Checks I Ran

I checked that Kali could reach the target and that the web apps responded.

Commands used:

```bash

ping -c 4 192.168.198.128

curl -I http://192.168.198.128:3000

curl -I http://192.168.198.128/DVWA

curl -I http://192.168.198.128/bWAPP
```
## Results

The ping test confirmed that Kali could reach the target VM.

OWASP Juice Shop responded on port 3000 with:
````text
HTTP/1.1 200 OK
````
DVWA responded with a redirect to the login page:
````text
HTTP/1.1 302 Found
````
bWAPP responded with a redirect to the portal page:
````text
HTTP/1.1 302 Found
````
These results confirmed that the target VM was reachable and that the lab web applications were running.

## Evidence

Screenshots for this lab are stored in:
````text
assets/screenshots/00-lab-setup/
````

**Evidence files:**
````text
01-shared-folder-mount-and-fstab.png
02-ping-target-host-only-success.png
03-curl-juiceshop-http-200.png
04-curl-dvwa-http-302-login-redirect.png
05-curl-bwapp-http-302-portal-redirect.png
````
## Notes

The testing stayed inside the local VMware lab.
No public systems or third-party targets were tested.

## Result

The lab environment was ready for the next labs.
