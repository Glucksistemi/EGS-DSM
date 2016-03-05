
from connections.telnet import get_authorized_connection
from connections.sockserver import SocketHandler
from schedule.timer import Timer
import settings
import imports
# TODO: Log handling (take it from my xlsx2xml and add log-leveling logic
parsers = imports.create_list_of_imported_objects(settings.PARSERS)
askers = imports.create_dict_of_imported_objects(settings.ASKERS)

telnet_connect = get_authorized_connection(settings.HOST, settings.PASSWORD, settings.TELNET_PORT)
tcp_connect = SocketHandler(settings.TCP_PORT, settings.SOCKET_CONTROL_LENGTH)
timer = Timer(settings.SCHEDULE)

break_condition = 0
waiting_asker = False
request_source = 0  # TODO: Constants for sources: 0 - none, 1 - parser, 2 - timer, 3 - tcp

try:
    while not break_condition:
        request = None
        line = telnet_connect.read_until('\r\n',0.1)
        if line:
            if waiting_asker:
                response, wait_flag = askers[waiting_asker].parse(line)
                if response and not wait_flag:
                    if request_source == 3:
                        tcp_connect.send_response(response)
                    waiting_asker = False
                    request_source = 0
                    continue
            for parser in parsers:
                request = parser.parse(line)
                if request:
                    request_source = 1
                    break # TODO: add check for unparsed string
        if not request:
            request = timer.iterate()
            request_source = 2
        if not request:
            request = tcp_connect.get_data_from_socket()
            request_source = 3
        if request:
            asker, asker_request = request.split(' ', 1)
            command, wait_flag = askers[asker].ask(asker_request)
            if command:
                telnet_connect.write(command + '\n')
                if wait_flag:
                    waiting_asker = asker
except:
    telnet_connect.close()
    raise
