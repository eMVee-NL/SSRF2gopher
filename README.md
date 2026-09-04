# SSRF2gopher
Gopher protocol is used a lot when exploiting SSRF. This script generates a gopher payload that can be used to replicate an HTTP request.
A Server-side Request Forgery (SSRF) vulnerability occurs when an attacker manipulates a server-side application into making HTTP requests to a domain of their choice, even internal applications can be a target.

Screenshot of new version
<img width="1897" height="726" alt="afbeelding" src="https://github.com/user-attachments/assets/9a063573-81e5-499e-8473-304a1f3108fc" />




## Usage
## CLI Usage

```bash
python3 SSRF2gopher.py [-h] [-u HOST] [-p PORT] [-e ENDPOINT] [-H [HEADERS ...]] [-m METHOD] [-d DATA]
```

## Options

| Option | Long Variant | Description |
| :--- | :--- | :--- |
| `-h` | `--help` | Show this help message and exit. |
| `-u` | `--host` | Target internal host address or domain name. |
| `-p` | `--port` | Gopher/HTTP port number on the target server. |
| `-e` | `--endpoint` | Target endpoint or path (e.g., `/index.php`). |
| `-H` | `--headers` | Custom headers in `"Name:Value"` format separated by spaces. |
| `-m` | `--method` | HTTP method to be used (GET, POST, PUT, etc.). Default: GET. |
| `-d` | `--data` | POST data body parameters (x-www-form-urlencoded). |

---

Enter the following details:
- Host, example `localhost`
- Port number on target (host) for gopher, example `80`
- Endpoint (path), example `/api/user/create/`
- Data what should be submitted something like, example `username=Hacker&password=Password1234&email=email@domain.tld`
- Method (POST, GET...)
- HTTP Headers (Header:value)



old screenshot
![image](https://github.com/eMVee-NL/SSRF2gopher/assets/45883753/55ce27c4-9f24-4c13-9212-3822fb7032e3)
