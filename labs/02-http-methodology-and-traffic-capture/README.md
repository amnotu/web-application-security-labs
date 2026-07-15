# Lab 02: HTTP and Traffic Capture

This lab documents my first HTTP checks and a basic packet capture.

The goal was to see how a web request looks from the terminal and how the traffic appears in a capture.

## Target

OWASP Juice Shop:

`http://192.168.198.128:3000`

## HTTP Check

I used `curl` to check the Juice Shop response headers.

Command used:

```bash

curl -I http://192.168.198.128:3000

```
