import argparse


def fib(n):
    # bool types in python can be evaulated as ints apparently
    if not isinstance(n, int) or n < 0 or isinstance(n, bool):
        return None
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help='Calculate the nth fibonacci number')
    args = parser.parse_args()

    nth = fib(args.n)
    print('fib({}) = {}'.format(args.n, nth))
