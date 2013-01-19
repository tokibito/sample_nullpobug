import argparse


def main():
    parser = argparse.ArgumentParser(description='This is description value.')
    parser.add_argument('arg1', metavar='A', type=int, nargs='+',
                        help='an int value')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the int(default: find the max)')
    args = parser.parse_args()
    print args.accumulate(args.arg1)


if __name__ == '__main__':
    main()
