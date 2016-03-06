import datetime
from core.settings import LOG_LEVELS, LOG_FILE

levels = {
    'error': 1,
    'warn': 2,
    'debug': 3
}

class Log:
    file = None
    params = {}

    def __init__(self):
        self.levels = LOG_LEVELS
        self.path = LOG_FILE
        if self.path:
            self.file = open(self.path.format(datetime.datetime.now().strftime('%Y%m%d-%H%M')), 'w')

    def log(self, level, logstr):
        pass

    def close(self):
        self.file.close()