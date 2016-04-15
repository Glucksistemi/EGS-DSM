from core.workers import Parser, ManyStringsParser
from core.connections.database.utils import save_playfield_change


class PlayerExitPFParser(ManyStringsParser):
    """parser for message when player leaves playfield. typical string = '05-09:42:00.000 Disconnecting client 1/Shpiler from Asteroid Field - now empty => enqueued for delayed unload'"""
    #regexp = r"^.*[Cc]lient .*\/'?(?P<nick_name>\w+).*from (?P<playfield>.+)(,|( -)).*$"
    regexp = {
        "disonnecting": r"^.*[Cc]lient .*\/'?(?P<nick_name>\w+).*from (?P<playfield>.+) -.*$",
        "disconnected": r"^.*[Cc]lient .*\/'?(?P<nick_name>\w+).*from (?P<playfield>.+),.*$"
    }
    # FIXME: WORKS WRONG WITH STRING LIKE 05-09:42:40.045 Client 1/'Shpiler' disconnected from Akua Orbit, now empty -> delayed unload enqueued

    def on_match(self, line, match_object, *args):
        print match_object.groupdict()
        save_playfield_change(0, nick_name=match_object.groupdict()['nick_name'], playfield=match_object.groupdict()['playfield'])
