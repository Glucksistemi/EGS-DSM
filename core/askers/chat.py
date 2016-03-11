from core.workers import Asker


class ChatAsker(Asker):
    request_name = 'say'
    regexp = "^Message '.*$' sent to all clients"

    def on_ask(self, request):
        return "say '" + request.replace("'", "`") + "'", True

    def on_response(self, match_object, response):
        return 'message sent', False
