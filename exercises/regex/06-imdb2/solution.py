import requests
import sys
import re


if len(sys.argv) < 2:
    print("At least one command line argument needed")
    sys.exit(-1)

year = int(sys.argv[1])

if len(sys.argv) >= 3:
    month = int(sys.argv[2])
else:
    month = 1

if len(sys.argv) >= 4:
    day = int(sys.argv[3])
else:
    day = 1



request = requests.get('http://250.took.nl/history/{}/{}/{}/full'.format(year, month, day))
match = re.search(r'<table class="list-data">(.*)</table>', request.text, re.DOTALL)
if match:
    list_data = match.group(1)

    for table_row in re.findall(r'<tr.*?>(.*?)</tr>', list_data, re.DOTALL):
        table_cols = re.findall(r'<td.*?>(.*?)</td>', table_row, re.DOTALL)

        if len(table_cols) == 6:
            rank = int(re.search(r'\d+', table_cols[0]).group(0))
            score = float(table_cols[2].strip())
            title = re.search(r'<a.*?>(.*?)</a>', table_cols[3]).group(1)
        
            print(rank, score, title)
else:
    print('No data found for {} {} {}'.format(year, month, day))
    sys.exit(-1)
