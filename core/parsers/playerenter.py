from core.workers import Parser


class HeartBeatParser(Parser):
    """parser for message when player enters. typical string = 'Player 76561198056103537/'Shpiler' logged in'"""
    regexp = '*Player ?P<Id>/\'?P<Id>\' logged in'

    def on_match(self, line, match_object, *args):
        print match_object.groupdict()