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
