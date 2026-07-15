# Lab 02: HTTP and Traffic Capture

## Objective

Review basic HTTP request and response behavior, connect the work to the PTES-style methodology, and capture traffic from the local lab environment.

## Methodology Phase

PTES Phase: Intelligence Gathering / Technical Enumeration

This lab focuses on observing how the tester machine communicates with the local target web application before deeper vulnerability testing begins.

## Scope

Testing is limited to the local VMware lab.

Included target:

- OWASP Juice Shop at `http://192.168.198.128:3000`

Excluded targets:

- Public systems

- Third-party applications

- Production environments

## Part 1: HTTP Observation with curl

A basic HTTP request was sent from Kali to OWASP Juice Shop.

Target:

`http://192.168.198.128:3000`

The response confirmed that the application was reachable and returned:

`HTTP/1.1 200 OK`



The response headers also showed common web server headers such as:

- `Content-Type`

- `Content-Length`

- `Cache-Control`

- `X-Frame-Options`

- `X-Content-Type-Options`

## Part 2: Verbose HTTP Request Flow

A verbose `curl` request was used to observe the request and response flow. This helped confirm the direction of traffic between the tester VM and the target web application.

Command used:
````bash
curl -v http://192.168.198.128:3000 -o /dev/null
````

## Part 3: Packet Capture

A short packet capture was created while sending HTTP requests to Juice Shop.

Capture target:

- Host: `192.168.198.128`

- Port: `3000`

- Protocol: TCP/HTTP

Capture command:
````bash
sudo timeout 15 tcpdump -i any -nn -s 0 -w labs/02-http-methodology-and-traffic-capture/evidence/juiceshop-basic-http.pcap 'host 192.168.198.128 and tcp port 3000'
````

The packet capture summary confirmed TCP traffic between:

- Kali: `192.168.68.131`

- Target: `192.168.198.128:3000`

The summary showed TCP connection setup, request/response packets, and connection closure.

## Route Observation

The route check showed Kali reaching the target through `eth0`:

`192.168.198.128 via 192.168.68.2 dev eth0 src 192.168.68.131`

This confirms that the traffic was sent from the Kali VM through its active network interface.

## Evidence

| Evidence | What it shows |
|---|---|
| [`http-juiceshop-curl-observation.txt`](evidence/http-juiceshop-curl-observation.txt) | HTTP headers and verbose curl request/response flow. |
| [`packet-capture-summary.txt`](evidence/packet-capture-summary.txt) | Safe summary of captured TCP traffic to Juice Shop. |
| [`01-http-juiceshop-curl-observation.png`](../../assets/screenshots/02-http-methodology-and-traffic-capture/01-http-juiceshop-curl-observation.png) | Screenshot of HTTP curl observation evidence. |
| [`02-packet-capture-summary.png`](../../assets/screenshots/02-http-methodology-and-traffic-capture/02-packet-capture-summary.png) | Screenshot of packet capture summary evidence. |
| `Localy/labs/02-http-methodology-and-traffic-capture/evidence/file.pcap & file0.pcapng`. | Local-only evidence |

## Security Notes

The raw packet capture is not committed to GitHub. Packet captures can contain cookies, tokens, credentials, request bodies, or other sensitive values depending on the test. The repository `.gitignore` excludes `.pcap` and `.pcapng` files.

The public evidence uses a short text summary instead of publishing the raw packet capture.


## Result

Basic HTTP observation and packet capture are complete.
