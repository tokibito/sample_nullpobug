import requests
import json
import os


def post_to_slack(event, context):
    env_dict = os.environ
    url = env_dict['ENDPOINT']
    payload = {
        'text': 'ボタンが押されました。',
    }
    requests.post(url, data=json.dumps(payload))
    return {'status': 'ok'}
