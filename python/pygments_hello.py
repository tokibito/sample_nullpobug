# coding: utf-8
import sys

from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import HtmlFormatter


def main():
    if len(sys.argv) < 2:
        sys.exit()
    infile = sys.argv[1]
    # 対象ファイルを読み込み
    with open(infile, 'rb') as f:
        code = f.read()
    # lexerを自動判定
    lexer = guess_lexer(code)
    lexer.encoding = 'utf-8'
    # formatterを用意
    formatter = HtmlFormatter(encoding='utf-8')
    # シンタックスハイライトを適用してprint
    print highlight(code, lexer, formatter)


if __name__ == '__main__':
    main()
