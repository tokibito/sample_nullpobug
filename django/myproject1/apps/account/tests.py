# coding: utf-8
from django.test import TestCase

from apps.account import api as account_api


class CheckPasswordTestCase(TestCase):
    def test_ok(self):
        self.assertTrue(account_api.check_password('test', '098f6bcd4621d373cade4e832627b4f6'))

    def test_invalid_password(self):
        self.assertFalse(account_api.check_password('invalid', '098f6bcd4621d373cade4e832627b4f6'))
