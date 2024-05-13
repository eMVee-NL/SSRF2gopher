# SSRF2gopher
Gopher protocol is used a lot when exploiting SSRF. This script generates a gopher payload what can be used to submit data to a webform.
A Server-side Request Forgery (SSRF) vulnerability occurs when an attacker manipulates a server-side application into making HTTP requests to a domain of their choice, even internal applications can be a target.

![image](https://github.com/eMVee-NL/SSRF2gopher/assets/45883753/55ce27c4-9f24-4c13-9212-3822fb7032e3)


_**Currently this script genererates only a payload for the POST method and it is not final yet.**_


## Usage
It's pretty simple to generate a payload, just start the script.
```
python3 SSRF2gopher.py
```
Enter the following details:
- Host, example `localhost`
- Port number on target (host) for gopher, example `80`
- Endpoint (path), example `/api/user/create/`
- Data what should be submitted something like, example `username=Hacker&password=Password1234&email=email@domain.tld`

The 'double' encoded payload can be usedto attack via the browser. _(This worked for me while testing locally)_
