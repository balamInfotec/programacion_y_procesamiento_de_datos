from pydantic import BaseModel, Field
from typing import Dict
from datetime import datetime

class Telemetry(BaseModel):
    deviceId: str = Field(..., description="ID del dispositivo IoT")
    timestamp: datetime = Field(..., description="Fecha y hora del dato")
    metrics: Dict[str, float] = Field(..., description="Diccionario de métricas")

"""
    Ejemplo de JSON válido:

    {
        "deviceId": "raspberry",
        "timestamp": "2026-09-18T19:20:00Z",
        "metrics": {
                "temperature": 42.7,
                "humidity": 55.2,
                "voltage": 3.3
            }
    }
"""

class Command(BaseModel):
    deviceId: str
    command: str
