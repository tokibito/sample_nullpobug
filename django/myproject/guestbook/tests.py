# coding: utf-8
from django.test import TestCase

from guestbook.models import Greeting


class GreetingModelTest(TestCase):
    def setUp(self):
        self.greeting = Greeting(content=u"a\n" * 30)

    def test_unicode(self):
        u"""__unicode__メソッドのテスト
        """
        result = unicode(self.greeting)
        # 改行が削除されて20文字までに切り詰められる
        self.assertEquals(result, u"a" * 20)
