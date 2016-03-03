from connections.telnet import get_logged_connection
from connections.tcp import SocketHandler
import settings
import imports

telnet_connect = get_logged_connection(settings.HOST, settings.PASSWORD, settings.TELNET_PORT)
tcp_connect = SocketHandler(settings.TCP_PORT, settings.SOCKET_CONTROL_LENGTH)

parsers = imports.create_list_of_imported_objects(settings.PARSERS)
askers = [] #TODO: write one-two basic askers and treat them like parsers

break_condition = 0

try:
    while not break_condition:
        line = telnet_connect.read_until('\r\n',1)
        print line
        if line:
            for parser in parsers:
                parser.parse(line)
        request = tcp_connect.get_data_from_socket()
        if request:
            for asker in askers:
                asker.

        
except:
    telnet_connect.close()
    raise



