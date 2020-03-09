import asyncio
import socketio

sio = socketio.AsyncClient(reconnection=False)


@sio.on('ping')
async def on_ping(data):
    print('on_ping: ', data)


@sio.event
async def connect():
    print('connected.')


@sio.event
async def disconnect():
    print('disconnected.')


async def main():
    await sio.connect('http://localhost:8000')
    await sio.wait()

asyncio.run(main())
