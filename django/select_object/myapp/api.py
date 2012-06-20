# coding: utf-8
from django.db import connection

from beproud.django.commons.utils.dbi import select

from myapp.models import Player
from myapp.mappers import PlayerMapper


def get_players_list():
    """すべてのプレイヤーのリストを返す
    """
    sql = """
  SELECT
    u.name,
    pa.age,
    pb.point
  FROM user u
  LEFT JOIN profile_a pa ON u.id = pa.user_id
  LEFT JOIN profile_b pb ON u.id = pb.user_id
"""
    result = select(connection, sql, model=Player)
    return [PlayerMapper(player).as_dict() for player in result]
