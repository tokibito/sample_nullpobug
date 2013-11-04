# coding: utf-8
import csv
try:
    # Python2.7ではcsv.writerがunicode対応ではないのでStringIOモジュールを使用する
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from bottle import get, response, run


@get('/download')
def download():
    """CSVファイルを作成してダウンロードさせる
    """
    stream = StringIO()
    writer = csv.writer(stream)
    writer.writerow(['foo', '123'])
    writer.writerow(['bar', '456'])
    # ストリームの読み書きの位置を先頭に変更する
    stream.seek(0)
    # Webブラウザがダウンロードしたファイルを保存するようにヘッダを指定する
    response.content_type = 'application/octet-stream'
    # ファイル名をtest.csvとする
    response.headers['Content-Disposition'] = "attachment; filename='test.csv'"
    return stream.getvalue()


if __name__ == '__main__':
    run(host='127.0.0.1', port=5000)
