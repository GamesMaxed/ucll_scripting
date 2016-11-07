from urllib.request import urlopen
import re
import sys

if len(sys.argv) != 2:
    sys.exit("Please specify url")

response = urlopen(sys.argv[1]).read()

for match in re.findall(r'href="([^?"]+)"', str(response)):
    print(match)
