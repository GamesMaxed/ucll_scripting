import os
from typing import List


def tree(path: str) -> str:
    def aux(path: str):
        lines: List[str] = []
        for entry in sorted(os.scandir(path), key=lambda x: x.name):
            if entry.is_file():
                lines.append(entry.name)
            else:
                lines.append("[{}]".format(entry.name))
                lines += ["  " + children for children in aux(entry.path)]
        return lines

    return "\n".join(aux(path))

if __name__ == '__main__':
    """
    Indien opgeroepen vanuit shell,
    moet het resultaat van tree(path)
    afprinten, waarbij path meegegeven
    wordt als command line argument.
    Indien er geen command line argument
    werd meegegeven, moet de tree
    van de huidige directory ('.')
    afgeprint worden.
    """
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, default='.', help='Path to the directory')
    path = parser.parse_args().path
    print(tree(path))