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
    for k, g in groupby(sorted(data, key=lambda v: v[0]), lambda v: v[0]):
        print '%s: %s' % (k, list(g))

if __name__ == '__main__':
    main()
