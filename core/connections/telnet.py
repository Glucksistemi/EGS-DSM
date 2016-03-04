from telnetlib import Telnet


def get_authorized_connection(host, password, port=30004):
    print 'start...'
    connection = Telnet(host, port)
    print 'connected'
    connection.read_until('password:')
    connection.write('pass\n')
    connection.read_until('reenter password:')
    connection.write(password + '\n')
    connection.read_until("\r\n= \r\n\r\n")
    print 'connection estabilished'
    return connection