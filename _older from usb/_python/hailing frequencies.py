import socket

def server():
    sock = socket.socket()

    IP = socket.gethostbyname(socket.gethostname())
    port = 10027

    sock.bind((IP, port))
    sock.listen(27)

    conn_sock, address = sock.accept()
    print('Connected. Waiting for message.')

    while True:
        print(conn_sock.recv(4096))

def client():
    sock = socket.socket()

    IP = 'IP here'
    port = 10027

    sock.connect((IP, port))
    print('Connected. Input messages.')

    while True:
        sock.sendall(input())

role = input('Role? \n')
if role == 'server' or role == 'reciever':
    server()
elif role == 'client' or role == 'transmitter':
    client()
else:
    print('No.')
