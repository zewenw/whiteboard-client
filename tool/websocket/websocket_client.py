import websocket
import asyncio


async def hello(num):
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send_msg('hello')
        recv_ = await websocket.recv()
        print(recv_)


def say_hello():
    for i in range(100):
        loop.run_until_complete(hello(i))


loop = asyncio.get_event_loop()

if __name__ == '__main__':
    say_hello()
