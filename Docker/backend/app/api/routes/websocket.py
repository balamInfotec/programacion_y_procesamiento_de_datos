from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.websocket_manager import ws_manager
import logging
from app.services.mqtt_client import mqtt_service
import json
from app.core.models import Command

logger = logging.getLogger("websocket")

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            message = await websocket.receive_text()

            # Intentar parsear JSON
            try:
                data = json.loads(message)
            except json.JSONDecodeError:
                logger.error("[WS] Mensaje no es JSON válido.")
                continue
            
            # Validamos con el modelo
            try:
                command = Command(**data)
            except Exception as e:
                logger.error(f"[WS] Comando inválido: {e}")
                continue

            mqtt_service.publish_command(command.deviceId, command.command)

    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
        logger.info("[WS] Cliente desconectado.")

