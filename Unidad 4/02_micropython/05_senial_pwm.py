from machine import Pin, PWM
from time import sleep

led = PWM(Pin(1))
led.freq(1000)

while True:
    for brillo in range(0, 65536, 4096):
        led.duty_u16(brillo)
        sleep(0.05)
        
    for brillo in range(65535, -1, -4096):
        led.duty_u16(brillo)
        sleep(0.05)