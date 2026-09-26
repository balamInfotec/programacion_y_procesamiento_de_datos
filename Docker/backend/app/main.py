
import logging
from fastapi import FastAPI
from app.api import api_router
from app.services.mqtt_client import mqtt_service
from app.core.logging_config import setup_logging
import asyncio

# Configura los formatos, niveles y destinos de los mensajes de logging.
setup_logging()
logger = logging.getLogger("backend")

# Crea la aplicación FastAPI y establece el título que aparecerá
# en la documentación automática de la API.
app = FastAPI(title="Backend IoT")

# Registra en la aplicación todas las rutas definidas en api_router.
app.include_router(api_router)

# Registra una función para ejecutarla cuando FastAPI termine de iniciar.
@app.on_event("startup")
def startup_event():
    logger.info("[APP] Iniciando aplicación FastAPI...")
    
    # Guardar el event loop de FastAPI
    # Esto servirá para la implementación del websocket, se puede saltar esto hasta que se implemente
    mqtt_service.loop = asyncio.get_event_loop()
    
    # Configura las credenciales y conecta el cliente con el broker MQTT.
    mqtt_service.connect()
    # Inicia el hilo de red que mantiene activa la comunicación MQTT.
    mqtt_service.loop_start()
    logger.info("[APP] Cliente MQTT iniciado.")

# Registra una función para ejecutarla cuando FastAPI comience a apagarse.
@app.on_event("shutdown")
def shutdown_event():
    logger.info("[APP] Apagando aplicación FastAPI...")
    # Detiene el hilo de red y la comunicación del cliente MQTT.
    mqtt_service.loop_stop()
    logger.info("[APP] Cliente MQTT detenido.")
