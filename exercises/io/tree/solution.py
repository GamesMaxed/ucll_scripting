import os


def tree(path = '.'):
    def aux(path):
        lines = []
        
        for entry in sorted(os.scandir(path), key=lambda x: x.name):
            if entry.is_file():
                lines.append(entry.name)
            elif entry.is_dir():
                lines.append("[{}]".format(entry.name))
                lines += [ "  " + line for line in aux(entry.path) ]

        return lines

    return "\n".join(aux(path))


print(tree('testdir/qux'))
