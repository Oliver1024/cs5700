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

with socket(AF_INET, SOCK_STREAM) as s:
    try:
        s.settimeout(1)
        s.connect((HOST, PORT))
        s.sendall(file_name.encode())
        data = s.recv(1024)

        print("Connection Successful!")
        print()
        print("---------------HTTP RESPONSE---------------")
        print(data.decode())
        print("---------------END OF HTTP RESPONSE---------------")

    except:
        print("Error while connecting!")
