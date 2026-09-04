# SSRF2gopher
Gopher protocol is used a lot when exploiting SSRF. This script generates a gopher payload that can be used to replicate an HTTP request.
A Server-side Request Forgery (SSRF) vulnerability occurs when an attacker manipulates a server-side application into making HTTP requests to a domain of their choice, even internal applications can be a target.

Screenshot of new version
<img width="1897" height="726" alt="afbeelding" src="https://github.com/user-attachments/assets/9a063573-81e5-499e-8473-304a1f3108fc" />




## Usage

```
usage: SSRF2gopher.py [-h] [-u HOST] [-p PORT] [-e ENDPOINT] [-H [HEADERS ...]] [-m METHOD]

Gopher payload generator with custom headers support

options:
  -h, --help            show this help message and exit
  -u, --host HOST       Target host address
  -p, --port PORT       Gopher port number
  -e, --endpoint ENDPOINT
                        Target endpoint
  -H, --headers [HEADERS ...]
                        Custom headers in format "Name:Value"
  -m, --method METHOD   HTTP method (GET, POST, PUT, etc.)
```

Enter the following details:
- Host, example `localhost`
- Port number on target (host) for gopher, example `80`
- Endpoint (path), example `/api/user/create/`
- Data what should be submitted something like, example `username=Hacker&password=Password1234&email=email@domain.tld`
- Method (POST, GET...)
- HTTP Headers (Header:value)
