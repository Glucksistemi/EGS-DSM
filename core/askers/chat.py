from core.workers import Asker
from core.connections.database.utils import save_chat_message


class ChatAsker(Asker):
    request_name = 'say'
    regexp = r"^Message '(?P<msg>.*)' sent to all clients$"

    def on_ask(self, request):
        string = "say '" + request.replace("'", "`") + "'"
        return string, True

    def on_response(self, line, result):
        save_chat_message(message=result.groupdict()['msg'])
        return 'message sent', False
