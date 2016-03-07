from core.workers import Parser
from core.connections.database.models import ChatMessage
from core.connections.database.utils import get_player
import datetime


class ChatParser(Parser):
    """parser for chat. 05-09:42:33.997 CHAT: Shpiler: ppp"""
    regexp = r'^[0-9:.-]{15} CHAT: (?P<nick_name>\w+): (?P<msg>.*)$'

    def on_match(self, line, match_object, *args):
        gdict = match_object.groupdict()
        ChatMessage.create(
            datetime=datetime.datetime.now(),
            player=get_player(gdict['nick_name']),
            message=gdict['msg']
        )