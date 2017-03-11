import sys


def plagiarism(files):
    def read(file):
        with open(file, 'r') as f:
            return set(f)

    contents = [ read(file) for file in files ]
    triplets = [ (files[i], files[j], len(contents[i] & contents[j])) for i in range(0, len(files)) for j in range(0, len(files)) if files[i] < files[j] ]

    return sorted(triplets, key=lambda x: (-x[2], x[0], x[1]))
    


if __name__ == '__main__':
    for (file1, file2, metric) in plagiarism(sys.argv[1:]):
        print("{} vs {} : {} lines in common".format(file1, file2, metric))
