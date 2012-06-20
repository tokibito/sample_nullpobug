# coding: utf-8
from pprint import pprint

from django.test import TestCase

from myapp import api
from myapp.models import User, ProfileA, ProfileB


class PlayersListTest(TestCase):
    def setUp(self):
        for i in range(3):
            user = User.objects.create(name='Player%d' % i)
            profile_a = ProfileA.objects.create(
                user=user,
                age=(i + 1) * 10  # 10, 20, 30
            )
            profile_b = ProfileB.objects.create(
                user=user,
                point=(i + 1) * 200  # 200, 400, 600
            )

    def test_call(self):
        lst = api.get_players_list()
        pprint(lst)
