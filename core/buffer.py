class TerminalBuffer(object):
    buffer = []

    def write_line(self, line):
        self.buffer.append(line)
        #print self.buffer
        if len(self.buffer) > 100:
            del self.buffer[0]

    def get_buffer(self):
        import json
        reply = json.dumps(self.buffer)
        print reply, type(reply)
        self.buffer = []
        return reply