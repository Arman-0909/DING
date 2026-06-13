from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from app.websocket.manager import manager

from app.db.session import get_db_session

from app.utils.token import verify_token

from app.services.message_service import (
    create_message
)

from app.services.chat_service import (
    is_chat_member
)

router = APIRouter()


@router.websocket(
    "/ws/chat/{chat_id}"
)
async def websocket_endpoint(
    websocket: WebSocket,
    chat_id: int
):

    token = websocket.query_params.get(
        "token"
    )

    print("TOKEN:", token)

    if not token:
        print("NO TOKEN")
        await websocket.close(
            code=1008
        )
        return

    payload = verify_token(
        token
    )

    print("PAYLOAD:", payload)

    if not payload:
        print("TOKEN INVALID")
        await websocket.close(
            code=1008
        )
        return

    sender_id = int(
        payload.get("sub")
    )

    print("SENDER:", sender_id)

    db = get_db_session()

    member = is_chat_member(
        db,
        chat_id,
        sender_id
    )

    print("MEMBER:", member)

    if not member:
        print("NOT MEMBER")
        await websocket.close(
            code=1008
        )
        db.close()
        return

    print("CONNECTED")

    await manager.connect(
        chat_id,
        websocket
    )

    try:

        while True:

            text = await websocket.receive_text()

            message = create_message(
                db=db,
                chat_id=chat_id,
                sender_id=sender_id,
                content=text
            )

            await manager.broadcast(
                chat_id,
                {
                    "id": message.id,
                    "chat_id": message.chat_id,
                    "sender_id": message.sender_id,
                    "content": message.content,
                    "created_at": str(
                        message.created_at
                    )
                }
            )

    except WebSocketDisconnect:

        manager.disconnect(
            chat_id,
            websocket
        )

    finally:

        db.close()