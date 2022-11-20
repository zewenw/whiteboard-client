import asyncio
import websockets


async def run(websocket, path):
    while True:
        recv_text = await websocket.recv()
        print("recv_text:",  recv_text)
        await websocket.send(recv_text)


async def main():
    # start a websocket server
    async with websockets.serve(run, "127.0.0.1", 8765):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
    # asyncio.get_event_loop().run_forever()
