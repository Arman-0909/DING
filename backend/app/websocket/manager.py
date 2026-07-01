import logging

from fastapi import WebSocket


logger = logging.getLogger(__name__)


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

        logger.info(
            "CONNECTED | Chat %s | Total: %s",
            chat_id,
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

            logger.info(
                "DISCONNECTED | Chat %s | Remaining: %s",
                chat_id,
                len(self.active_connections[chat_id])
            )

    async def broadcast(
        self,
        chat_id: int,
        message: dict
    ):
        if chat_id not in self.active_connections:
            return

        stale = []

        for connection in self.active_connections[chat_id]:
            try:
                await connection.send_json(
                    message
                )
            except Exception:
                logger.warning(
                    "Stale connection in chat %s, removing",
                    chat_id
                )
                stale.append(connection)

        for connection in stale:
            self.active_connections[chat_id].remove(
                connection
            )


manager = ConnectionManager()