import socket
from egsdsm_backend.egsdsm_backend.settings import SOCKET_CONNECTION


def tcp_request(string):
    if not string:
        return ''
    sock = socket.socket()
    sock.connect(SOCKET_CONNECTION)
    sock.send(str(len(string)).zfill(5) + string)
    length = sock.recv(5)
    response = sock.recv(int(length))
    sock.close()
    return response

