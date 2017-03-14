import sys


def next_generation(bs):
    """
    Rekent de volgende generatie uit voor de gegeven
    string bs, die bestaat uit uitsluitend 0'en en 1'en.
    """
    table = { '111': '0',
              '110': '1',
              '101': '0',
              '100': '1',
              '011': '1',
              '010': '0',
              '001': '1',
              '000': '0' }
    
    rs = [ None ] * len(bs)
    bs = bs[0] + bs + bs[-1]

    for i in range(len(rs)):
        rs[i] = table[bs[i:i+3]]

    return "".join(rs)


def compute_n_generations(bs, n):
    """
    Rekent n generaties uit.
    """
    for _ in range(n):
        bs = next_generation(bs)

    return bs


def process_file(file):
    n = int(file.readline())

    for _ in range(n):
        bs = file.readline().strip()
        ngens = int(file.readline())

        print(compute_n_generations(bs, ngens))


if __name__ == '__main__':
    process_file(sys.stdin)
