def increment(input, output):
    while not input.end_reached():
        x = input.read()
        output.write(x + 1)

def double(input, output):
    while not input.end_reached():
        x = input.read()
        output.write(x * 2)
