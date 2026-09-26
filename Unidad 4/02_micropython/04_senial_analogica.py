from machine import ADC
from time import sleep

sensor = ADC(26)

while True:
    # El valor leído está entre 0 y 65535
    valor = sensor.read_u16()
    # La placa trabaja con un voltaje entre 0 y 3.3v
    voltaje = valor * 3.3 / 65535
    print(f"Valor analógico: {valor}, voltaje: {voltaje}")
    
    sleep(1)




