import time

def slow_response(data: bytes, interval: int) -> iter:
    """
    指定された時間だけスリープして1バイトずつデータを返すジェネレータ
    """
    for byte in data:
        time.sleep(interval)
        yield byte.to_bytes()

def application(environ, start_response):
    """
    WSGIアプリケーション
    """
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
    ]
    start_response(status, headers)
    return slow_response(b'Hello\n', 1)