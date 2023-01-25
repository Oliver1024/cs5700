import socket
import sys

def main():
    host = '127.0.0.1'
    port = 5000
    message=int(sys.argv[1])
    if message < -1000 or message > 1000:
        return
    s = socket.socket()
    s.connect((host, port))

    s.send(message.to_bytes(2, byteorder='big', signed=True))
    data = int.from_bytes(s.recv(1024), byteorder='big', signed=True)
    print("Sent ", message,"and received b'",data,"'")
    s.close()

if __name__ == '__main__':
    main()

