import asyncio
import websockets


TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZXhwIjoxNzgxMzYwMDY4fQ.lnHhaC_mz5mxAPGxm2U4RENNuUlM52YakZhd8cTMXeo"


async def main():

    uri = (
        f"ws://127.0.0.1:8000/ws/chat/1"
        f"?token={TOKEN}"
    )

    async with websockets.connect(
        uri
    ) as ws:

        print("Connected ✅")

        while True:

            message = input(
                "You: "
            )

            await ws.send(
                message
            )

            response = await ws.recv()

            print(
                "Received:",
                response
            )


asyncio.run(main())