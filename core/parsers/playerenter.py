from core.workers import Parser
from core.connections.database.utils import save_logon_event


class PlayerEnterParser(Parser):
    """parser for message when player enters. typical string = '[PA] Player 76561198056103537/'Shpiler' logged in'"""
    regexp = r"^[0-9:.-]{15} \[..] Player (?P<steam_id>\d+)\/'(?P<nick_name>\w+)' logged in$"

    def on_match(self, line, match_object, *args):
        print match_object.groupdict()
        save_logon_event(1, **match_object.groupdict())
