from core.workers import Parser
from core.connections.database.utils import save_playfield_change


class PlayerEnterPFParser(Parser):
    """parser for message when player enters playfield. typical string = '05-09:42:40.045 Client 1/'Shpiler' disconnected from Akua Orbit, now empty -> delayed unload enqueued'"""
    regexp = r"^.*[Cc]lient .*\/(?P<nick_name>\w+) .* from (?P<playfield>.*)[( -),].*$"

    def on_match(self, line, match_object, *args):
        print match_object.groupdict()
        save_playfield_change(1, nick_name=match_object.groupdict()['nick_name'], playfield=match_object.groupdict()['playfield'])
