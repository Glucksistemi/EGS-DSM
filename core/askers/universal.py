from core.workers import Asker


class UniversalAsker(Asker):
    def on_ask(self, request):
        return request, False