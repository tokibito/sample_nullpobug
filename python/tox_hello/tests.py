# coding: utf-8
from unittest import TestCase


def add(a, b):
    return a + b


class AddTestCase(TestCase):
    def testInt(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(5, 10), 15)
        self.assertEqual(add(-10, 10), 0)

    def testStr(self):
        self.assertEqual(add("abc", "def"), "abcdef")
