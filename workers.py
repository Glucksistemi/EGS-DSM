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
    response_parser = Parser()
    wait_for_response = False

    def __init__(self):
        pass

    def on_ask(self, *args, **kwargs):
        self.wait_for_response = True
        #todo: prepare string for writing, send it to writer's bufer or whatever

    def on_response(self, response):
        pass
