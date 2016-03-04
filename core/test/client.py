import socket
port = raw_input('enter local port to connect')

try:
    while True:
        sock = socket.socket()
        strng = raw_input(':>')
        sock.connect(('localhost', port))
        sock.send(str(len(strng)).zfill(5) + strng)
        length = int(sock.recv(5))
        print sock.recv(length)
        sock.close()
except:
    try:
        sock.close()
    except NameError:
        pass
    raise