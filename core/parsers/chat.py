from core.workers import Parser


class ChatParser(Parser):
    """parser for chat. 05-09:42:33.997 CHAT: Shpiler: ppp"""
    regexp = r'^[0-9:.-]{15} CHAT: (?P<nick_name>\w+): (?P<msg>.*)$'

    def on_match(self, line, match_object, *args):
        print match_object.groupdict()