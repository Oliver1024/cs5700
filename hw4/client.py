# Kejian Tong

import socket
import sys

HOST = "127.0.0.1" #The server's host name or IP address
PORT = 65432 #The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    url = sys.argv[1]
    s.sendall(url.encode('utf-8'))
    data = s.recv(1024)
    print(data.decode('utf-8'))
    s.close()
