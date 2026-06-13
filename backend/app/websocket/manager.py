from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        self.active_connections = {}

    async def connect(
        self,
        chat_id: int,
        websocket: WebSocket
    ):
        await websocket.accept()

        if chat_id not in self.active_connections:
            self.active_connections[chat_id] = []

        self.active_connections[chat_id].append(
            websocket
        )

        print(
            f"CONNECTED | Chat {chat_id} | Total:",
            len(self.active_connections[chat_id])
        )

    def disconnect(
        self,
        chat_id: int,
        websocket: WebSocket
    ):
        if chat_id in self.active_connections:

            if websocket in self.active_connections[chat_id]:
                self.active_connections[chat_id].remove(
                    websocket
                )

            print(
                f"DISCONNECTED | Chat {chat_id} | Remaining:",
                len(self.active_connections[chat_id])
            )

    async def broadcast(
        self,
        chat_id: int,
        message: dict
    ):
        print(
            "\nBROADCASTING:",
            message
        )

        if chat_id not in self.active_connections:
            print("NO ACTIVE CONNECTIONS")
            return

        print(
            "CONNECTIONS:",
            len(
                self.active_connections[chat_id]
            )
        )

        for connection in self.active_connections[chat_id]:
            await connection.send_json(
                message
            )

        print("BROADCAST COMPLETE")



manager = ConnectionManager()