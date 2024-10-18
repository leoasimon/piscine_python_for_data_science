import sys
from ft_filter import ft_filter


def is_greater_than(min: int):
    return lambda w: len(w) > min


def parse_args():
    args = sys.argv[1:]
    if len(args) != 2:
        print('AssertionError: the arguments are bad')
        return None

    try:
        n = int(args[1])
        # print(n)
        s = args[0]
        return (s, n)
    except ValueError:
        print('AssertionError: the arguments are bad')
        return None


def main():
    args = parse_args()

    if args is None:
        return 1

    (s, n) = args

    words = s.split(' ')
    res = ft_filter(is_greater_than(n), words)

    print(res)


if __name__ == '__main__':
    main()
