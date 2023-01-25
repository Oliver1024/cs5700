# Kejian Tong
#Client program to send data to a server via a socket, and then have that same data echoed back.
import socket
import sys

HOST = "127.0.0.1" #The server's host name or IP address
PORT = 65432 #The port used by the server
message = int(sys.argv[1])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Create a new socket using teh given address famiily, socket
    #type and protocol number
    s.connect((HOST, PORT)) #Connect to a remote socket at the address and port
    if message < -1000 or message > 1000:
        exit()
    s.send(message.to_bytes(2, byteorder='big', signed=True)) #Send data to the socket. The socket must be connected to a remote socket. Data type
    #is byte
    data = int.from_bytes(s.recv(1024), byteorder='big', signed=True) #Receive data from the socket. The return type is a bytes object representing the data received.
    #The maximum amount of data to be received in each chunk is 1024 as specified.
    print(f"Sent {message} and received b'{data}'") #print to console