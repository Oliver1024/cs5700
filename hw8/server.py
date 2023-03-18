# Kejian Tong

from socket import *
import sys

# Retrieve the port number from command line arguments
if len(sys.argv) < 2:
    print("Please provide the port number.")
    sys.exit(1)

try:
    PORT = int(sys.argv[1])
except ValueError:
    sys.exit(1)

HOST = gethostbyname(gethostname())

print(f"Server IP address: {HOST}\r\n")
print(f"Server port number: {PORT}\r\n\r\n")
print("Ready to server...")

# Create a socket and bind it to the specified port
with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    # Listen for incoming connections
    s.listen()

    while True:
        # Accept a new connection
        conn, addr = s.accept()
        with conn:
            # Receive the client's request
            data = conn.recv(1024)
            if data:
                file_name = data.decode()
                try:
                    with open(file_name, 'rb') as content:
                        conn.sendall("HTTP/1.1 200 OK \n\n".encode() + content.read())
                except:
                    conn.sendall("HTTP/1.1 404 Not Found".encode())
