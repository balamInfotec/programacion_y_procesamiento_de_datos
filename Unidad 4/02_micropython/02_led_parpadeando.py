"""
    Configuración de salida digital
"""
from machine import Pin
from time import sleep

# Configramos el pin como salida digital
led = Pin("LED", Pin.OUT)

while True:
    led.value(1)
    print("Led encendido")
    sleep(1)
    led.value(0)
    print("Led apagado")
    sleep(1)