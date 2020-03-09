# python-socketioとfastapiを組み合わせるサンプル

## サーバーの起動

```
uvicorn server:app_socketio
```

## クライアントの起動

```
python client.py
```

## curlでAPI呼び出し

```
curl -w '\n' http://localhost:8000/ping/<sid>
```
