# coding: utf-8
from itertools import groupby

data = (
    (1, 10),
    (2, 20),
    (2, 5),
    (1, 2),
    (4, 7),
    (3, 1),
    (2, 100),
)

def main():
    results = {}
    for k, g in groupby(data, lambda v: v[0]):
        for v in g:
            results[k] = results.get(k, 0) + v[1]
    # print
    for k, v in results.items():
        print '%s: %s' % (k, v)

if __name__ == '__main__':
    main()
