import asyncio
import websockets

websocket_users = set()


async def run(websocket, path):
    flag = True
    while flag:
        try:
            websocket_users.add(websocket)
            recv_text = await websocket.recv()
            # print("recv_text:",  recv_text)
            for socket in websocket_users:
                if socket != websocket:
                    await socket.send(recv_text)
                    print("send_text:", recv_text)
        except Exception as e:
            websocket_users.remove(websocket)
            print("Exception:", e)


async def main():
    # start a websocket server
    async with websockets.serve(run, "127.0.0.1", 8765):
        await asyncio.Future()  # run forever


if __name__ == '__main__':
    asyncio.run(main())
    # asyncio.get_event_loop().run_forever()
