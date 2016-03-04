
from connections.telnet import get_authorized_connection
from connections.sockserver import SocketHandler
import settings
import imports
# TODO: Log handling (take it from my xlsx2xml and add log-leveling logic
telnet_connect = get_authorized_connection(settings.HOST, settings.PASSWORD, settings.TELNET_PORT)
tcp_connect = SocketHandler(settings.TCP_PORT, settings.SOCKET_CONTROL_LENGTH)

parsers = imports.create_list_of_imported_objects(settings.PARSERS)
askers = imports.create_list_of_imported_objects(settings.ASKERS)

break_condition = 0

try:
    while not break_condition:
        line = telnet_connect.read_until('\r\n',1)
        print line
        if line:
            for parser in parsers:
                parser.parse(line)
        request = tcp_connect.get_data_from_socket()
        for asker in askers:
            if asker.wait_for_response:
                tcp_connect.send_response(asker.parse(line, telnet_connect))
            if request:
                command = asker.ask(request)
                if command:
                    telnet_connect.write(command + '\n')

        
except:
    telnet_connect.close()
    raise



