import sys
import re

for line in sys.stdin:
    if not re.match('#', line):
        print(line, end='', flush=True)
