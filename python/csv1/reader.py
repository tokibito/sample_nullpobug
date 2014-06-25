# coding: utf-8
import csv


def main():
    with open('data.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for idx, value in enumerate(row):
                print u"{}: {}".format(idx + 1, value.decode('cp932'))
            print "-" * 10

if __name__ == '__main__':
    main()
