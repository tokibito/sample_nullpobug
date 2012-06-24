# coding: utf-8
import code
import readline
import rlcompleter


def hello():
    print("Hello, world!")


def main():
    print(u"対話コンソールを起動します...")
    # コンソール起動時の変数を用意
    variables = globals()

    # Tabによる補完を有効にする
    readline.set_completer(rlcompleter.Completer(variables).complete)
    readline.parse_and_bind("tab:complete")

    # 対話コンソールを開始
    code.interact(local=variables)


if __name__ == '__main__':
    main()
