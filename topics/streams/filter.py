import sys
import re

while True:
    line = input()

    if not re.match('#', line):
        print(line)
