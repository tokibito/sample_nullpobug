# coding: utf-8
from google.appengine.ext.webapp import util

cachevar = None  # キャッシュ用変数
def application(environ, start_response):
    global cachevar
    if cachevar is None:
        msg = '%s'
        cachevar = []
        for i in range(10):
            cachevar.append(i)
            # 意図的に例外を発生させる
            #if i == 5:
            #    from google.appengine.runtime import DeadlineExceededError
            #    raise DeadlineExceededError
    else:
        msg = 'hit: %s'

    start_response('200 OK', [('Content-Type', 'text/plain')])
    return msg % str(cachevar)

def main():
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
