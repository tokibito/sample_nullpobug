from django.contrib.sessions.models import Session
from django.conf import settings
from django.core.signing import b64_encode
from django.utils.crypto import salted_hmac


def run(*args):
    session_key = "4u5wt8aenukp3t2bvifvobneuft32c6y"
    session_record = Session.objects.filter(session_key=session_key).first()
    print(f"DjangoのSECRET_KEY: {settings.SECRET_KEY}")
    print(f"データベース上のsession_key: {session_record.session_key}")
    print(f"データベース上のsession_data: {session_record.session_data}")
    session_store_class = session_record.get_session_store_class()
    print(f"セッションストアクラス: {session_store_class}")
    session_store = session_store_class()
    print(f"セッションストアのsalt: {session_store.key_salt}")
    breakpoint()
    result, timestamp = session_record.session_data.rsplit(":", 1)
    salted_hmac_value = b64_encode(salted_hmac(
        session_store.key_salt + "signer",
        result,
        secret=settings.SECRET_KEY,
    ).digest())
    print(f"セッションストアのsalted_hmac値: {salted_hmac_value}")
    print(f"デコードされたセッションデータ: {session_record.get_decoded()}")