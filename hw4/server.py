# Kejian Tong
#A simple program that will create a server that would echo a client request back to the client

import socket

HOST = "127.0.0.1" #Standard loopback interface address (localhost)
PORT = 65432 #Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Create a new socket using the given address family,
    # socket type, and protocol number
    s.bind((HOST, PORT)) #Bind the socket to an address and port number. The socket must not already be bound.
    s.listen() #Enable a server to accept connections.
    conn, addr = s.accept() #Accept a connection. The socket must be bound to an address and listening for connections.
    #The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on
    #the connection, and address is the address bound to the socket on the other end of the connection.
    with conn: #with keyword is used for unmanaged resources such as socket stream or file stream, used for exception
        #handling
        print(f"Connected by {addr}") #prints the client's connection address
        while True: #looping the input stream to receive all byte data from the client
            data = conn.recv(1024)
            if not data:
                break #breaks out once no more data to receive
            data = int.from_bytes(data, byteorder='big', signed=True) #receives the data from the client
            sum = data + 100
            conn.send(sum.to_bytes(2, byteorder='big', signed=True)) 