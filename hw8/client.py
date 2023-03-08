import socket
import sys

# Retrieve the server IP address, port number, and file name from command line arguments
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
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print("Connection Successful!")
    except (ConnectionRefusedError, socket.gaierror):
        print("Error while connecting!")
        sys.exit(1)

    # Send a GET request for the specified file
    request = f"GET /{file_name} HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
    s.sendall(request.encode())

    # Receive the server's response
    response = s.recv(1024).decode()

    # If the response contains a not found error, print an error message and exit
    if "HTTP/1.1 404 Not Found\r\n" in response:
        print("---------------HTTP RESPONSE---------------")
        print("HTTP/1.1 404 Not Found")
        print("---------------END OF HTTP RESPONSE---------------")
        sys.exit(1)
    # If the response contains a success message, print it
    if "HTTP/1.1 200 OK\r\n" in response:
        print("---------------HTTP RESPONSE---------------")
        print("HTTP/1.1 200 OK")
        file_content = response.split("\r\n\r\n")[1]
        print(file_content.strip())
        print("---------------END OF HTTP RESPONSE---------------")