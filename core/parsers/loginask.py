from core.workers import Parser
from core.connections.database.utils import save_logon_event


class LoginAskParser(Parser):
    """parser for message when player ask for enter. typical string = '05-09:38:28.768 [PA] Player 76561198056103537/'Shpiler' asking for login'"""
    regexp = r"^[0-9:.-]{15} \[..] Player (?P<steam_id>\d+)\/'(?P<nick_name>\w+)' asking for login$"

    def on_match(self, line, match_object, *args):
        print match_object.groupdict()
        save_logon_event(0, **match_object.groupdict())
