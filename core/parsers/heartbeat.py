from core.workers import Parser
from core.connections.database.handler import save_heartbeat


class HeartBeatParser(Parser):
    """parser for heartbat. typical string = '02-10:33:34.633 Uptime=47h46m heap=26.9MB fps=41.6 players=1'"""
    regexp = r'^(?P<date>[0-9:.-]{15}) Uptime=(?P<hours>\d+)h(?P<minutes>\d+)m heap=(?P<heap>[0-9.]+)MB fps=(?P<fps>[0-9.]+) players=(?P<players>\d+)$'

    def on_match(self, line, match_object, *args):
        print match_object.groupdict()
        groupdict = match_object.groupdict()
        del groupdict['date']
        save_heartbeat(**groupdict)