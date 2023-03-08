import socket
import sys

# Retrieve the port number from command line arguments
if len(sys.argv) < 2:
    print("Please provide the port number.")
    sys.exit(1)

try:
    PORT = int(sys.argv[1])
except ValueError:
    print("Invalid port number.")
    sys.exit(1)

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)

# Print the server's IP address and port number
print(f"Server IP address: {HOST}")
print(f"Server port number: {PORT}")

# Create a socket and bind it to the specified port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
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
                # Try to open the requested file and read its contents
                with open(file_name, "rb") as f:
                    file_contents = f.read()

                # If the file was found, send a success response with the file contents
                response = f"HTTP/1.1 200 OK\r\nConnection Successful!\r\nContent-Length: {len(file_contents)}\r\n\r\n"
                response += file_contents.decode()
                conn.sendall(response.encode())

            except FileNotFoundError:
                # If the file was not found, send a not found error response
                response = "HTTP/1.1 404 Not Found\r\nConnection Successful!\r\n\r\n"
                conn.sendall(response.encode())

            # except:
            #     # If there was an error, send an internal server error response
            #     response = "HTTP/1.1 500 Internal Server Error\r\nConnection Successful!\r\n\r\n"
            #     conn.sendall(response.encode())
