from telnet import get_logged_connection
import time
import settings
import imports
parsers = imports.create_list_of_imported_objects(settings.PARSERS)
connection = get_logged_connection(settings.HOST, settings.PASSWORD)
break_condition = 0

try:
    while not break_condition:
        line = connection.read_until('\r\n',1)
        print line
        if line:
            for parser in parsers:
                parser.parse(line)
        
except:
    connection.close()
    raise



