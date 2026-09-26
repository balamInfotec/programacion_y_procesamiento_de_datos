# Importa el módulo estándar de Python para crear y administrar registros
# de actividad de la aplicación.
import logging

# Importa la función que aplica una configuración de logging definida
# mediante un diccionario.
from logging.config import dictConfig

# Diccionario con la configuración completa del sistema de logging.
# Cada clave determina una parte del comportamiento de los registros:
# formateadores, manejadores, loggers y logger raíz.
LOGGING_CONFIG = {
    # Versión del formato de configuración de logging de Python.
    "version": 1,
    # Conserva activos los loggers creados por otras librerías, como Uvicorn.
    "disable_existing_loggers": False,

    # Define cómo se construye visualmente cada mensaje de log.
    "formatters": {
        # Formato breve para los mensajes mostrados normalmente en consola.
        "default": {
            # levelname: nivel del mensaje; name: nombre del logger;
            # message: contenido del mensaje.
            "format": "[%(levelname)s] %(name)s: %(message)s"
        },
        # Formato ampliado, útil para diagnosticar errores y localizar
        # el archivo y la línea que generaron el mensaje.
        "detailed": {
            # asctime: fecha y hora; filename: archivo; lineno: número de línea.
            "format": "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s"
        }
    },

    # Define los destinos a los que se enviarán los mensajes de log.
    "handlers": {
        # Handler que escribe los mensajes en la salida estándar del proceso.
        "console": {
            # Implementación estándar para enviar logs a la consola.
            "class": "logging.StreamHandler",
            # Utiliza el formato breve definido anteriormente.
            "formatter": "default",
        }
    },

    # Configura el comportamiento de loggers identificados por nombre.
    "loggers": {
        # Logger utilizado por la aplicación backend.
        "backend": {
            # Envía sus mensajes al handler llamado console.
            "handlers": ["console"],
            # Registra mensajes INFO, WARNING, ERROR y CRITICAL.
            "level": "INFO",
            # Evita reenviar estos mensajes al logger raíz y duplicarlos.
            "propagate": False
        },
        # Logger utilizado para registrar eventos relacionados al websocket
        "websocket": {
            # Envía sus mensajes al handler llamado console.
            "handlers": ["console"],
            # Registra mensajes INFO, WARNING, ERROR y CRITICAL.
            "level": "INFO",
            # Evita reenviar estos mensajes al logger raíz y duplicarlos.
            "propagate": False
        },
        # Logger utilizado para registrar eventos relacionados con MQTT.
        "mqtt": {
            # Envía sus mensajes al handler llamado console.
            "handlers": ["console"],
            # Registra mensajes INFO, WARNING, ERROR y CRITICAL.
            "level": "INFO",
            # Evita reenviar estos mensajes al logger raíz y duplicarlos.
            "propagate": False
        },
        # Logger de errores internos de Uvicorn.
        "uvicorn.error": {
            # Muestra los mensajes de nivel INFO o superior.
            "level": "INFO"
        },
        # Logger de solicitudes HTTP atendidas por Uvicorn.
        "uvicorn.access": {
            # Muestra los registros de acceso de nivel INFO o superior.
            "level": "INFO"
        }
    },

    # Configuración predeterminada para cualquier logger sin una configuración
    # específica, incluidas librerías externas.
    "root": {
        # Envía los mensajes al handler de consola.
        "handlers": ["console"],
        # Solo muestra WARNING, ERROR y CRITICAL para reducir ruido.
        "level": "WARNING"
    }
}

# Aplica LOGGING_CONFIG al sistema global de logging de Python.
def setup_logging():
    dictConfig(LOGGING_CONFIG)
