import socket

def main():
    host = "127.0.0.1"
    port = 5000
    backlog = 10
    bufsize = 4096

    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversock.bind((host, port))
    serversock.listen(10)

    print 'Waiting for connection...'
    clientsock, client_address = serversock.accept()
    print 'CONNECTED'

    while True:
        rcvmsg = clientsock.recv(bufsize)
        print 'Received -> %s' %(rcvmsg)
        print 'Type message...'
        sendmsg = raw_input()
        print 'Wait...'
        clientsock.sendall(sendmsg)
    clientsock.close
    return

if __name__ == '__main__':
    main()