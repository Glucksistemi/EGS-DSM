from core.workers import Asker
from core.log import log


class SaveAndExitAsker(Asker):
    request_name = 'saveandexit'
    regexp = '^Saving and exiting...$'

    def on_ask(self, request):
        log.log('error', 'safe shutdown server by asker')
        return 'saveandexit', False
