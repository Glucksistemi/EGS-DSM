# Telnet login data
HOST = 'shpiler.net'
TELNET_PORT = 30004
PASSWORD = 'JebKerman'

# TCP params
SOCKET_CONTROL_LENGTH = 5
TCP_PORT = 42404

# workers collections
PARSERS = (
    'parsers.heartbeat.HeartBeatParser',
    'parsers.playerenter.PlayerEnterParser',
)
ASKERS = {
    'chat': 'core.askers.chat.ChatAsker',
}

SCHEDULE = (
    {
        'command': 'chat test command',
        'name': 'test',
        'repeater': 'interval',
        'params': {
            'interval': 60,  # seconds
        }
    },
)

DATABASE = {
    'type': 'mysql',  # available: sqlite, postgress
    'name': 'egsdsm',  # database/schema name
    'params': {  # parameters for connection
        'host': 'localhost',
        'user': 'egsdsm',
        'password': '123QWErty'
    }
}

LOG_LEVEL_DEBUG = 3
LOG_LEVEL_WARN = 2
LOG_LEVEL_ERROR = 1

LOG_LEVELS = {
    'database': LOG_LEVEL_ERROR,
    'file': LOG_LEVEL_WARN,
    'stdout': LOG_LEVEL_DEBUG,
}

LOG_FILE = '/home/gluck/dsm{}.log'