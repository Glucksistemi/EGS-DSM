from telnetlib import Telnet


def get_logged_connection(host, password, port=30004):
    connection = Telnet(host, port)
    connection.read_until('password:')
    connection.write('pass\n')
    connection.read_until('reenter password:')
    connection.write(password + '\n')
    connection.read_until("\r\n= \r\n\r\n")
    print 'connection estabilished'
    return connection