from chalice import Chalice
import requests
import json
import os

app = Chalice(app_name='send to slack')
app.debug = True


@app.route('/')
def index():
    env_dict = os.environ
    url = env_dict['ENDPOINT']
    payload = {
        'text': 'ボタンが押されました。',
    }
    requests.post(url, data=json.dumps(payload))
    return {'status': 'ok'}
