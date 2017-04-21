import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--end', type=int, default=float('inf'))
    parser.add_argument('--skip-empty', action='store_true', default=False)
    args = parser.parse_args()

    with open(args.file, 'r') as file:
        index = 0
        for line in file:
            line = line.rstrip()
            
            if args.start <= index and index <= args.end:
                if not args.skip_empty or line:
                    print(line)
            index += 1
