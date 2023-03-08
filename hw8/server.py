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

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)

print(f"Server IP address: {HOST}")
print(f"Server port number: {PORT}")

# Create a socket and bind it to the specified port
with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    # Listen for incoming connections
    s.listen()

    while True:
        # Accept a new connection
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")

            # Receive the client's request
            data = conn.recv(1024)

            # Parse the request to get the requested file name
            request = data.decode()
            file_name = request.split()[1][1:]

            try:
                with open(file_name, "rb") as f:
                    file_contents = f.read()
                response = f"HTTP/1.1 200 OK\r\nConnection Successful!: {len(file_contents)}\r\n\r\n"
                response += file_contents.decode()
                conn.sendall(response.encode())

            except FileNotFoundError:
                response = "HTTP/1.1 404 Not Found\r\nConnection Successful!\r\n\r\n"
                conn.sendall(response.encode())
