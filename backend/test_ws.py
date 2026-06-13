import asyncio
import websockets


async def main():

    async with websockets.connect(
        "ws://127.0.0.1:8000/ws/chat/1/1"
    ) as ws:

        while True:

            msg = input("You: ")

            await ws.send(msg)

            response = await ws.recv()

            print("Received:", response)


asyncio.run(main())