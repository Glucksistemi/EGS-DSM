from core.workers import Parser
from core.connections.database.models import HeartBeat
import datetime


class HeartBeatParser(Parser):
    """parser for heartbat. typical string = '02-10:33:34.633 Uptime=47h46m heap=26.9MB fps=41.6 players=1'"""
    regexp = r'^(?P<date>[0-9:.-]{15}) Uptime=(?P<hours>\d+)h(?P<minutes>\d+)m heap=(?P<heap>[0-9.]+)MB fps=(?P<fps>[0-9.]+) players=(?P<players>\d+)$'

    def on_match(self, line, match_object, *args):
        groupdict = match_object.groupdict()
        uptime = int(groupdict['hours']) * 60 + int(groupdict['minutes'])
        del groupdict['date']
        HeartBeat.create(
            datetime = datetime.datetime.now(),
            uptime=str(uptime),
            heap=float(groupdict['heap']),
            fps=float(groupdict['fps']),
            players=int(groupdict['players'])
        )