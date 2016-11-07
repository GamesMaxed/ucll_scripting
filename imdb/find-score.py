import re
import sys

title = sys.argv[1]

with open("ratings.list", "r") as ratings:
    for line in ratings:
        match = re.search(title, line, re.I)
        if match:
            match = re.search(r'(\d\.\d)\s+(.*)', line)
            print("{} : {}".format(match.group(2), match.group(1)))

