import socket


class SocketHandler():
    socket = None
    connection = None
    control_length = 5

    def __init__(self, port, control_length=5):
        self.socket = socket.socket()
        self.socket.bind(('', port))
        self.control_length = control_length
        self.socket.listen(1)

    def get_data_from_socket(self):
        try: # avoid timeout errors to allow looping
            self.connection, address = self.socket.accept()
            self.connection.settimeout(1)
            req_len = int(self.connection.recv(5))
        except socket.timeout:
            req_len = 0
        if req_len:
            return self.connection.recv(req_len)
        else:
            return None

    def send_response(self, response):
        length = str(len(response)).zfill(5)
        self.connection.send()

    def close(self):
        self.socket.close()



