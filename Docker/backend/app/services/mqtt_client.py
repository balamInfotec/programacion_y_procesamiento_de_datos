# Importa el módulo estándar de Python para registrar eventos y errores.
import logging
import asyncio
import json

# Importa el cliente MQTT de Paho, utilizado para comunicarse con Mosquitto.
import paho.mqtt.client as mqtt

from app.services.websocket_manager import ws_manager

# Importa la configuración cargada desde las variables de entorno o .env.
from app.core.config import settings

# Importamos el modelo de validación de los datos desde mosquitto
from app.core.models import Telemetry

# Crea un logger identificado como "mqtt" para registrar eventos MQTT.
logger = logging.getLogger("mqtt")

# Encapsula la conexión y las operaciones MQTT utilizadas por el backend.
class MQTTService:
    # Inicializa el cliente MQTT y registra los callbacks que se ejecutarán
    # cuando se conecte al broker o llegue un mensaje.
    def __init__(self):
        # Crea una instancia del cliente MQTT de Paho.
        self.client = mqtt.Client()

        # Asocia on_connect al evento de conexión con el broker.
        self.client.on_connect = self.on_connect

        # Asocia on_message al evento de recepción de mensajes.
        self.client.on_message = self.on_message

    # Configura las credenciales y establece la conexión con el broker MQTT.
    def connect(self):
        # Configura el usuario y la contraseña definidos en settings.
        self.client.username_pw_set(settings.mqtt_username, settings.mqtt_password)

        # Conecta al host y puerto definidos en las variables de entorno.
        # El tercer argumento indica un keepalive de 60 segundos.
        self.client.connect(settings.mqtt_broker_host, settings.mqtt_broker_port, 60)

    # Inicia el hilo de red de Paho para mantener la conexión activa y
    # procesar mensajes entrantes sin bloquear el hilo principal de FastAPI.
    def loop_start(self):
        self.client.loop_start()

    # Detiene el hilo de red de Paho y la comunicación MQTT del cliente.
    def loop_stop(self):
        self.client.loop_stop()

    # Callback ejecutado automáticamente después de intentar conectarse.
    # client: cliente MQTT conectado.
    # userdata: datos definidos por la aplicación, si existen.
    # flags: indicadores enviados por el broker.
    # rc: código numérico con el resultado de la conexión.
    def on_connect(self, client, userdata, flags, rc):
        # Registra el código recibido del broker.
        logger.info(f"Conectado al broker MQTT con código: {rc}")

        # Se suscribe al tópico configurado para recibir mensajes publicados allí.
        client.subscribe(settings.mqtt_topic)

    # Callback ejecutado cada vez que llega un mensaje de un tópico suscrito.
    # msg contiene el tópico, el payload y otros metadatos del mensaje.
    def on_message(self, client, userdata, msg):
        # Convierte el payload recibido, que llega como bytes, a texto UTF-8.
        payload = msg.payload.decode()

        # Obtiene el nombre del tópico donde se publicó el mensaje.
        topic = msg.topic

        # Registra el tópico y el contenido del mensaje recibido.
        logger.info(f"[MQTT] Mensaje recibido en {topic}: {payload}")
        
        # Intentar parsear JSON
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            logger.error("[MQTT] Payload no es JSON válido.")
            return

        # Validar con Pydantic
        try:
            telemetry = Telemetry(**data)
        except Exception as e:
            logger.error(f"[MQTT] Telemetría inválida: {e}")
            return
        
        # Ejecutar broadcast en el event loop de FastAPI
        if hasattr(self, "loop"):
            asyncio.run_coroutine_threadsafe(
                ws_manager.broadcast(telemetry.json()),
                self.loop
            )
        else:
            logger.error("[MQTT] No se encontró event loop para WebSocket.")
            
    def publish_command(self, device_id: str, payload: str):
        topic = f"devices/{device_id}/commands"
        logger.info(f"[MQTT] Publicando comando en {topic}: {payload}")
        self.client.publish(topic, payload)



# Crea una instancia compartida del servicio para reutilizar el mismo cliente
# MQTT en el resto de la aplicación.
mqtt_service = MQTTService()
