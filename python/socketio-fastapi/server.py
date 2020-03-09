import socketio
from fastapi import FastAPI

# setup fastapi
app_fastapi = FastAPI()
# setup socketio
sio = socketio.AsyncServer(async_mode='asgi')
app_socketio = socketio.ASGIApp(sio, other_asgi_app=app_fastapi)


@app_fastapi.get("/")
async def index():
    """fastapiのAPI実装(socketioに関係ない)
    """
    return {"result": "Index"}


@app_fastapi.get("/ping/{sid}")
async def ping(sid: str):
    """指定されたsidにemitするエンドポイント
    """
    sio.start_background_task(
        sio.emit,
        "ping", {"message": "ping from server"}, room=sid)
    return {"result": "OK"}


@sio.event
async def connect(sid, environ):
    """socketioのconnectイベント
    """
    print('connect ', sid)


@sio.event
async def disconnect(sid):
    """socketioのdisconnectイベント
    """
    print('disconnect ', sid)
