import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    while True:
        data = c.recv(1024)
        if not data:
            break
        data = int.from_bytes(data, byteorder='big', signed=True)
        sum = data + 100
        c.send(sum.to_bytes(2, byteorder='big', signed=True))
    c.close()

if __name__ == '__main__':
    main()

