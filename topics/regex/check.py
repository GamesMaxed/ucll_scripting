def check(string):
    parts = string.split(" ")

    if len(parts) != 4:
        return False
    if any(len(part) != 4 for part in parts):
        return False
    if parts[0][0:2] != "BE":
        return False
    if not all(s.isdigit() for s in parts[0][2:4]):
        return False
    if not all( all(c.isdigit() for c in part) for part in parts[1:]):
        return False

    return True

        
