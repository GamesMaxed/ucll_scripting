def increment(input, output):
    while not input.end_reached():
        x = int(input.readline())
        output.write(str(x + 1))

def double(input, output):
    while not input.end_reached():
        x = int(input.readline())
        output.write(str(x * 2))
