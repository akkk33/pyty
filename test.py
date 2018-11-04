import re

ex = re.compile('^[a-z\.\*]+$')

print(ex.match(''))