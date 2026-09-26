"""
    RECEPCION DE DATOS SERIAL CON PYTHON

    Este programa recibe mensajes enviados por la Raspberry Pi Pico W
    u otro dispositivo mediante un puerto serial USB.

    Instalacion de la libreria requerida:
        pip install pyserial

    Configura el puerto en la variable "puerto" antes de ejecutar el programa.
"""

# La libreria pyserial se instala con:
# pip install pyserial
import serial


def recibir_datos(puerto: str) -> None:
    """Abre el puerto y muestra los mensajes recibidos."""

    # serial.Serial recibe:
    # - puerto: nombre del puerto conectado a la Pico W.
    # - 9600: velocidad en baudios; debe coincidir con la configuracion
    #   utilizada por uart.write() en la Raspberry Pi Pico W.
    # - timeout=1: espera como maximo un segundo por cada lectura.
    with serial.Serial(puerto, 9600, timeout=1) as conexion:
        print(f"Escuchando datos en {puerto}...")
        print("Presiona Ctrl+C para terminar.")

        while True:
            # readline espera hasta recibir un salto de linea.
            datos = conexion.readline()

            if datos:
                # decode convierte los bytes recibidos en texto.
                # errors="replace" evita que un byte invalido detenga el programa.
                mensaje = datos.decode("utf-8", errors="replace").strip()
                print(f"Recibido: {mensaje}")


puerto = "COM5"
recibir_datos(puerto)
