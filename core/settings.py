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
)
ASKERS = {
    'chat': 'core.askers.chat.ChatAsker',
}

SCHEDULE = (
    {
        'command': '',
        'name': '',
        'params': {
            'interval': 3600,  # seconds
        }
    },
)