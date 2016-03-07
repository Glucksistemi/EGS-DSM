import re

regexp =r'^[0-9:.-]{15} CHAT: (?P<nick_name>\w+): (?P<msg>.*)$'

string = "05-09:42:33.997 CHAT: Shpiler: ppp"

rg = re.match(regexp, string)
if rg:
    print 'match:)'
    print rg.groupdict()
else:
    print 'no match:('
