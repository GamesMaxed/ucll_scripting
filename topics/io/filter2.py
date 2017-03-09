import sys
import re

while True:
    line = input()

    if not re.match(sys.argv[1], line):
        print(line)
