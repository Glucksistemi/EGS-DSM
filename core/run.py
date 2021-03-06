from connections.telnet import get_authorized_connection
from connections.sockserver import SocketHandler
from schedule.timer import Timer
import settings
import imports
from log import log
from time import sleep
from buffer import TerminalBuffer


parsers = imports.create_list_of_imported_objects(settings.PARSERS)
askers = imports.create_dict_of_imported_objects(settings.ASKERS)


telnet_connect = get_authorized_connection(settings.HOST, settings.PASSWORD, settings.TELNET_PORT)
tcp_connect = SocketHandler(settings.TCP_PORT, settings.SOCKET_CONTROL_LENGTH)
timer = Timer(settings.SCHEDULE)
terminal_buffer = TerminalBuffer()

break_condition = 0
waiting_asker = False #name of asker waiting for answer (or False if no asker waiting)
request_source = 0  # TODO: Constants for sources: 0 - none, 1 - parser, 2 - timer, 3 - tcp

try:
    while not break_condition:
        request = None  # request - variable with asker's name and string given to asker separated by space
        try:
            line = telnet_connect.read_until('\r\n',0.1)
        except:
            try:
                telnet_connect = get_authorized_connection(settings.HOST, settings.PASSWORD, settings.TELNET_PORT)
            except:
                log.log('error', 'no socket connection. retry in 5 seconds...')
                sleep(5)
            continue
        if line:
            log.log('debug', 'line: '+line)
            terminal_buffer.write_line(line)
            line = line.replace('\r\n', '')  # no EOL - no cross-platform problems;)
            if waiting_asker:  # first - give the line to waiting asker (if any)
                asker_response = askers[waiting_asker].parse(line) # give line to the asker
                if asker_response is not None:
                    response, wait_flag = asker_response
                    if response and not wait_flag:
                        if request_source == 3:  # if request came from TCP - send responce back and drop vars
                            tcp_connect.send_response(response)
                        waiting_asker = False
                        request_source = 0

            for parser in parsers:  # loop through parsers
                request = parser.parse(line)
                if request:
                    request_source = 1 #asker called from parser
                    break
        if not request:  # if parsers left no request, ask from timers
            request = timer.iterate()
            request_source = 2
        if not request:  # no request from parsers or timer? Try to get it from TCP
            request = tcp_connect.get_data_from_socket()
            if request == 'get_terminal_buffer':
                request = None
                tcp_connect.send_response(terminal_buffer.get_buffer())
            request_source = 3
        if request:  # so if there's a request from any source...
            asker, asker_request = request.split(' ', 1)
            try:
                command, wait_flag = askers[asker].ask(asker_request)  # ...give it to the asker
            except KeyError:
                log.log('warn', 'call for unregistered asker: '+ asker)
                command = ''
            if command: # and if asker gave us some response - feed it to the telnet
                log.log('debug', command)
                telnet_connect.write(command.encode('utf-8') + '\n')
                if wait_flag:  # and if asker told us to keep flag - let's keep it
                    waiting_asker = asker
            if request_source == 3 and not wait_flag:
                tcp_connect.send_response('empty')
        else:
            request_source = 0
except:
    telnet_connect.close()
    tcp_connect.close()
    try:
        log.log('error', 'DSM Stopped')
    except:
        pass
    log.close()
    raise
