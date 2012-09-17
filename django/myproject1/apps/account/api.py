# coding: utf-8
import hashlib


def check_password(raw_password, hash_value):
    """パスワードチェック
    """
    if not raw_password:
        return False
    return hashlib.md5(raw_password).hexdigest() == hash_value
