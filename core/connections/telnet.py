from telnetlib import Telnet
from log import log

def get_authorized_connection(host, password, port=30004):
    log.log('debug', 'connecting...')
    connection = Telnet(host, port)
    connection.read_until('password:')
    connection.write('pass\n')
    connection.read_until('reenter password:')
    connection.write(password + '\n')
    connection.read_until("\r\n= \r\n\r\n")
    log.log('error', 'connection estabilised')
    return connection
