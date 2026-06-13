import asyncio
import websockets


TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzgxMzYyMjI4fQ.riJLpjjKl2PoLEw_HE0X1xi_3gddk6pO7jb-3R2FO-A"


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

#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzgxMzYwMDM4fQ.DnNb2YiNaFZ7_gtvbHk5NXOo695kr2xCw5VArcnqQfs