# Kejian Tong

from socket import *
import sys

if len(sys.argv) < 4:
    print("Please provide the server IP address, port number, and file name.")
    sys.exit(1)

HOST = sys.argv[1]
try:
    PORT = int(sys.argv[2])
except ValueError:
    sys.exit(1)

file_name = sys.argv[3]

# Create a socket and connect to the server
with socket(AF_INET, SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print("Connection Successful!")
    except (ConnectionRefusedError, gaierror):
        print("Error while connecting!")
        sys.exit(1)

    # Send a GET request for the specified file
    request = f"GET /{file_name} HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
    s.sendall(request.encode())

    # Receive the server's response
    response = s.recv(1024).decode()

    if "HTTP/1.1 404 Not Found\r\n" in response:
        print("\r\n")
        print("---------------HTTP RESPONSE---------------")
        print(response.split('\r\n')[0])
        print("---------------END OF HTTP RESPONSE---------------")
        sys.exit(1)
    if "HTTP/1.1 200 OK\r\n" in response:
        # Split the response into headers and body
        headers, body = response.split("\r\n\r\n", 1)
        print("\r\n")
        # headers = headers.split('\r\n')
        # headers = [h for h in headers if not h.startswith('Content-Length') and not h.startswith('Connection Successful!')]
        print("---------------HTTP RESPONSE---------------")
        # print('\r\n'.join(headers))
        print(response.split('\r\n')[0])
        print("\r\n")
        print(body.strip())
        print("---------------END OF HTTP RESPONSE---------------")
