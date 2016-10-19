import socket
from contextlib import closing

def main():
    host = '127.0.0.1'
    port = 5000
    bufsize = 4096
                
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
        sock.send(b'Hello world')
        print(sock.recv(bufsize))

    return

if __name__ == '__main__':
    main()