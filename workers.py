import re

class Parser():
    regexp = ''
    def __init__(self):
        self.regexp_object = re.compile(self.regexp)

    def parse(self, line):
        result = self.regexp_object.match(line)
        if result:
            self.on_match(line, result)

    def on_match(self, line, match_object):
        pass