from typing import List
from fastapi import WebSocket
import logging

logger = logging.getLogger("websocket")

class WebSocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"[WS] Nueva conexión. Total: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            logger.info(f"[WS] Conexión cerrada. Total: {len(self.active_connections)}")

    async def broadcast(self, message: str):
        logger.info(f"[WS] Enviando mensaje a {len(self.active_connections)} clientes.")
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.error(f"[WS] Error enviando mensaje: {e}")
                self.disconnect(connection)

ws_manager = WebSocketManager()
