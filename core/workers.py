import re


class RegexpDriven():
    regexp = ''
    regexp_object = None
    onmatch_method_name = ''

    def __init__(self):
        self.regexp_object = re.compile(self.regexp)
        self.on_init()

    def on_init(self):
        pass

    def parse(self, line, *args):
        result = self.regexp_object.match(line)
        if result:
            try:
                return getattr(self, self.onmatch_method_name, '')(result, line, *args)
            except AttributeError:
                return None
            except TypeError:
                return None


class Parser(RegexpDriven):
    onmatch_method_name = 'on_match'

    def on_match(self, match_object, line, *args):
        pass


class Asker(RegexpDriven):
    request_name = '' # first word of request sent by server
    regexp = '' # regexp to parse response from server
    wait_for_response = False
    onmatch_method_name = 'on_response'


    def ask(self, request):
        if request.split[1] == self.request_name:
            return self.on_ask(request)
        else:
            return None

    def on_ask(self, request):
        """
        this method must return string with command which will be sent to the server.
        it takes request argument - string came from the tcp request
        Default behavior is sending input string without changes.
        """
        return request

    def on_response(self, match_object, response, connection):
        pass