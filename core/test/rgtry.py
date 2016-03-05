import re

regexp = ''
string = ''

rg = re.match(regexp, string)
if rg:
    print 'match:)'
    print rg.groupdict()
else:
    print 'no match:('
