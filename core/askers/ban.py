from core.workers import Asker


class BanAsker(Asker):
    request_name = 'ban'
    regexp = "^ '.*$' "  # TODO: write regexp

    def on_ask(self, request):
        return "ban '" + request.replace("'", "`") + "'", True

    def on_response(self, match_object, response):
        return 'player bannned', False
