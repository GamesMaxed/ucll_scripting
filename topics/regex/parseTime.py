def parseTime(str):
    pattern = r"(\d\d):(\d\d):(\d\d)\.(\d\d\d)"
    match = re.fullmatch(pattern, str)

    if match:
        h = int( match.group(1) )
        m = int( match.group(2) )
        s = int( match.group(3) )
        ms = int( match.group(4) )

        return (h, m, s, ms)
    else:
        return None

