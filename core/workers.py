import re
#from log import log


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
            log.log('error', 'wrong onmatch (AttributeError)')
            return None
        except TypeError:
            log.log('error', 'wrong onmatch (TypeError)')
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
                return self.call_onmatch_metod(line, result, name)


class Parser(RegexpDriven):
    onmatch_method_name = 'on_match'

    def on_match(self, match_object, line, *args):
        pass


class ManyStringsParser(ManyRegexpDriven):
    onmatch_method_name = 'on_match'

    def on_match(self, regex_name, match_object, line, *args):
        """
        :param regex_name: name of regexp in regexp dict which was matched
        :param match_object:
        :param line:
        :return:
        """
        pass


class Asker(RegexpDriven):
    regexp = '' # regexp to parse response from server
    onmatch_method_name = 'on_response'

    def ask(self, request):  # let it be - just to keep logic in names
        return self.on_ask(request)

    def on_ask(self, request):
        """
        this method must return string with command which will be sent to the server.
        it takes single argument - string came from the tcp request
        Default behavior is sending input string without changes.
        """
        return request, True

    def on_response(self, match_object, response):
        """
        function called under following circumstances:
        - on_ask were called before and returned wait_flag = True
        - EGS server got a command, returned by on_ask and send some string back
        - this string from EGS server matched self.regexp
        :param match_object: re.match object with results of matching regexp.
        :param response: string came by telnet, untouched
        :return: response for TCP if needed (it must be non-empty string, 'ok' by default, wait_asker flag
        """
        return 'ok', False


class ManyStringsAsker(ManyRegexpDriven, Asker):
    pass

