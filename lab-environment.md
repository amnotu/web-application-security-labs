# Lab Environment

This page documents the local lab setup I used for the project.

## Host

The lab runs on a Windows 11 host using VMware Workstation Pro.

## Attacker VM

The attacker machine is Kali Linux.

Kali was used for terminal work, HTTP checks, traffic capture, scanning, and documentation.

## Target VM

The target VM contains deliberately vulnerable web applications used for practice.

Applications used in this repo:

- OWASP Juice Shop
- DVWA
- bWAPP

## Network

Testing was done inside the local VMware network.

The target applications were reached through private lab IP addresses. No public targets were tested.

## Evidence Notes

Some local files are intentionally not committed, including packet captures, course-provided files, and raw data that could contain sensitive values.

The repo only keeps public-safe summaries and screenshots.
