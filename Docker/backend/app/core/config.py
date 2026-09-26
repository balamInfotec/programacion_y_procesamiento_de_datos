# Importa BaseSettings, que permite cargar valores de configuración
# desde variables de entorno y desde un archivo .env.
from pydantic_settings import BaseSettings

# Agrupa toda la configuración que utilizará la aplicación.
class Settings(BaseSettings):
    # Nombre o dirección del contenedor donde se ejecuta el broker MQTT.
    mqtt_broker_host: str
    # Puerto TCP que utiliza el broker MQTT.
    mqtt_broker_port: int
    # Tópico MQTT al que el backend se suscribirá o en el que publicará.
    mqtt_topic: str
    # Usuario utilizado por el backend para autenticarse en el broker MQTT.
    mqtt_username: str
    # Contraseña utilizada por el backend para autenticarse en el broker MQTT.
    mqtt_password: str

    # Configuración interna de Pydantic Settings.
    class Config:
        # Indica que también debe leer las variables definidas en el archivo .env.
        env_file = ".env"

# Crea una instancia global con la configuración validada de la aplicación.
# Al crearse, Pydantic busca los valores requeridos y verifica sus tipos.
settings = Settings()
