# Flaskで巨大なファイルをアップロードする例

Python 2.7, 3.6

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
unicorn main:app -c config.py
```

- nginx + gunicorn + Flaskを想定
- nginx, gunicorn, flaskでバッファリングせずに直接ファイルに書き出している。
  - ストリームを変更すれば他のところにも書き出し可能
- nginxのbodyの最大サイズ設定とバッファしない設定も必要
- jQuery File upload採用
