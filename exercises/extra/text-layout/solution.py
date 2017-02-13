import re


def split_lines_monospaced(string, line_width):
    words = re.split(r'\s+', string)

    lines = []
    current_line_length = line_width

    for word in words:
        new_line_length = current_line_length + 1 + len(word)

        if new_line_length <= line_width:
            lines[-1] += " " + word
            current_line_length = new_line_length
        else:
            lines.append(word)
            current_line_length = len(word)

    return lines
