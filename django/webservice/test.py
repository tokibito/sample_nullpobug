# coding: utf-8
import os
import urlparse
import urllib

from suds.client import Client

def path2url(path):
    return urlparse.urljoin(
      'file:', urllib.pathname2url(path))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WSDL_PATH = path2url(os.path.join(BASE_DIR, 'service.wsdl'))


def main():
    cli = Client(
        WSDL_PATH,
        location='http://localhost:8000/foo_service/',
        cache=None)

    print cli
    print "--------"

    result = cli.service.say_hello(u'こんにちは', 3)
    print "cli.service.say_hello(u'こんにちは', 3)"
    print "--- result ---"
    print result
    print "--- print ---"
    for v in result.string:
        print unicode(v)

    result = cli.service.item_all()
    print "cli.service.item_all()"
    print "--- result ---"
    print result
    print "--- print ---"
    if result:
        for item in result[0]:
            print u"name:{} value:{} updated_at:{}".format(item.name, item.value, item.updated_at)


if __name__ == '__main__':
    main()
