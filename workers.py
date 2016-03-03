import re


class Parser():
    regexp = ''
    regexp_object = None
    def __init__(self):
        self.regexp_object = re.compile(self.regexp)
        self.on_init()

    def parse(self, line):
        result = self.regexp_object.match(line)
        if result:
            self.on_match(line, result)

    def on_match(self, line, match_object):
        pass

    def on_init(self):
        pass


class Asker():
    request_name = ''
    response_parser = Parser()
    wait_for_response = False

    def __init__(self):
        pass

    def ask(self, request):
        if request.split[1] == self.request_name:
            self.on_ask(request)

    def on_ask(self, request):
        self.wait_for_response = True
        #todo: prepare string for writing, send it to writer's bufer or whatever

    def on_response(self, response):
        pass
