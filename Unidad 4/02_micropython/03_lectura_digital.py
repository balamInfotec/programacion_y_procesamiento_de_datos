from machine import Pin
from time import sleep

boton = Pin(14, Pin.IN)
led = Pin("LED", Pin.OUT)

while True:
    estado = boton.value()
    
    if estado == 1:
        led.value(1)
        print("Señal digital: botón presionado")
    else:
        led.value(0)
        print("Señal digital: botón no presionado")
        
    sleep(0.2)