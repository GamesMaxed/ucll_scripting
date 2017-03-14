import sys
import re

while True:
    line = input()

    if not re.match(`\pgfmark{sysargv start}`sys.argv[1]`\pgfmark{sysargv end}`, line):
        print(line)
