from core.workers import Parser


class HeartBeatParser(Parser):
    """parser for message when player enters. typical string = '[PA] Player 76561198056103537/'Shpiler' logged in'"""
    regexp = r"^\[..] Player (?P<ID>\d+)\/'(?P<name>\w+)' logged in$"

    def on_match(self, line, match_object, *args):
        print match_object.groupdict()