import socket
from egsdsm_backend.settings import SOCKET_CONNECTION


def tcp_request(string):
    print string
    if not string:
        return ''
    sock = socket.socket()
    sock.connect(SOCKET_CONNECTION)
    string = string.encode('utf-8')
    print str(len(string)).zfill(5) + string
    sock.send(str(len(string)).zfill(5) + string)
    length = sock.recv(5)
    response = sock.recv(int(length))
    sock.close()
    return response

