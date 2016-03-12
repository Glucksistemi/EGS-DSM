import datetime
from core.settings import LOG_LEVELS, LOG_FILE
from core.connections.database.models import CoreLog


class Log:
    file = None
    params = {}
    levels = {}
    lnums = {
        'error': 1,
        'warn': 2,
        'debug': 3
    }

    def __init__(self):
        self.levels = LOG_LEVELS
        self.path = LOG_FILE
        if self.path:
            self.file = open(self.path.format(datetime.datetime.now().strftime('%Y%m%d-%H%M')), 'w')

    def log(self, level, logstr):
        if type(level) is str:
            level = self.lnums[level]
        if self.levels['file'] and self.levels['file'] >= level:
            self.file.write(datetime.datetime.now().strftime('%Y %m %d-%H:%M') + ' ' + logstr)
        if self.levels['stdout'] and self.levels['stdout'] >= level:
            print datetime.datetime.now().strftime('%Y %m %d-%H:%M') + ' ' + logstr
        if self.levels['database'] and self.levels['database'] >= level:
            CoreLog.create()

    def close(self):
        self.file.close()

log = Log()