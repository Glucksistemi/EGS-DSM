import re


class RegexpDriven():
    regexp = ''
    regexp_object = None
    onmatch_method_name = ''

    def __init__(self, **kwargs):
        self.regexp_object = re.compile(self.regexp)
        self.on_init()

    def on_init(self):
        pass

    def parse(self, line):
        result = self.regexp_object.match(line)
        if result:
            return self.call_onmatch_metod(line, result)

    def call_onmatch_metod(self, *args, **kwargs):
        try:
            return getattr(self, self.onmatch_method_name, '')(*args, **kwargs)
        except AttributeError:
            return None
        except TypeError:
            return None


class ManyRegexpDriven(RegexpDriven):
    regexp = {}
    regexp_object = {}

    def __init__(self):
        for name, regex in self.regexp.iteritems():
            self.regexp_object[name] = re.compile(regex)
        self.on_init()

    def parse(self, line):
        for name, rg in self.regexp_object:
            result = rg.match(line)
            if result:
                return self.call_onmatch_metod(line,result, name)


class Parser(RegexpDriven):
    onmatch_method_name = 'on_match'

    def on_match(self, match_object, line, *args):
        pass


class Asker(RegexpDriven):
    request_name = '' # first word of request sent by server
    regexp = '' # regexp to parse response from server
    onmatch_method_name = 'on_response'

    def ask(self, request):
        if request.split()[0] == self.request_name:
            return self.on_ask(request)
        else:
            return None, None

    def on_ask(self, request):
        """
        this method must return string with command which will be sent to the server.
        it takes request argument - string came from the tcp request
        Default behavior is sending input string without changes.
        """
        return None, None

    def on_response(self, match_object, response):
        return None, None