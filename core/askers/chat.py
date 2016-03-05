from core.workers import Asker


class ChatAsker(Asker):
    request_name = 'say'
    regexp = '$Message...' # TODO: write regexp

    def on_ask(self, request):
        return "say '" + request.replace("'", "`") + "'"

    def on_response(self, match_object, response, connection):
        return 'message sent'