# coding: utf-8
import csv


def main():
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        # DictReaderのシーケンスは辞書を返す
        # 辞書のキーは1行目が使われる
        for record in reader:
            for key, value in record.items():
                print u"{}: {}".format(key, value.decode('cp932'))
            print "-" * 10

if __name__ == '__main__':
    main()
