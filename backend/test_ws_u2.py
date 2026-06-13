import asyncio
import websockets

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZXhwIjoxNzgxMzYyMzIwfQ.r9Te0TuL-_EIk2p9IDb0RgaLml2NvM7Pum1iDFYGyuM"


async def receive_messages(ws):
    while True:
        try:
            message = await ws.recv()
            print(f"\nReceived: {message}")
        except:
            break


async def send_messages(ws):
    while True:
        text = input("You: ")
        await ws.send(text)


async def main():

    uri = (
        f"ws://127.0.0.1:8000/ws/chat/1"
        f"?token={TOKEN}"
    )

    async with websockets.connect(uri) as ws:

        print("Connected ✅")

        await asyncio.gather(
            receive_messages(ws),
            send_messages(ws)
        )


asyncio.run(main())