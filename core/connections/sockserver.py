import socket


class SocketHandler():
    socket = None
    connection = None
    control_length = 5
    test_other_try = 0

    def __init__(self, port, control_length=5):
        if self.test_other_try:  # why I did it? J_0
            raise Exception('some bullshit happened')
        self.socket = socket.socket()
        self.socket.bind(('', port))
        self.socket.settimeout(0.1)
        self.control_length = control_length
        self.socket.listen(1)
        self.test_other_try = 1

    def get_data_from_socket(self):
        try: # avoid timeout errors to allow looping
            self.connection, address = self.socket.accept()
            self.connection.settimeout(1)
            req = self.connection.recv(5)
            print req
            req_len = int(req)
        except socket.timeout:
            req_len = 0
        if req_len:
            return self.connection.recv(req_len)
        else:
            return None

    def send_response(self, response):
        length = str(len(response)).zfill(5)
        self.connection.send(length+response)

    def close(self):
        self.socket.close()

