from unittest import TestCase

#from unittest import SkipTest
from nose.plugins.skip import SkipTest


def setUpModule():
    raise SkipTest


class MyTestCase(TestCase):
    def test(self):
        self.assertEqual(1 + 1, 2)
