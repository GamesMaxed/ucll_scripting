import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', type=int, default=0)
    parser.add_argument('--to', type=int, required=True)
    parser.add_argument('--step', type=int, default=1)
    args = parser.parse_args()

    for i in range(args.init, args.to+1, args.step):
        print(i)
    
