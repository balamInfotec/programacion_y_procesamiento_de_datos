"""
    Los diccionarios son estructuras de datos que permiten almacenar pares de clave-valor. 
    Cada clave es única y se utiliza para acceder a su valor correspondiente. 
    Los diccionarios son muy útiles para organizar y manipular datos de manera eficiente.
"""
sensor = {"temperatura": 25, "humedad": 60, "presion": 1013, "velocidad": None}

print(f"Sensor: {sensor}")
print(f"Temperatura: {sensor['temperatura']}")
print(f"Humedad: {sensor['humedad']}")
print(f"Presión: {sensor['presion']}")
print(f"Velocidad: {sensor['velocidad']}")
# Esto generará un KeyError porque la clave 'velocidad' no existe en el diccionario
# print(f"Clave no existente: {sensor['velocidad']}")

print(f"Clave no existente: {sensor.get('velocidad', 'Clave no encontrada')}")  # Usando get() para evitar KeyError

for clave, valor in sensor.items():
    print(f"{clave}: {valor}")
    
for clave in sensor.keys():
    print(f"Clave: {clave}")
    
for valor in sensor.values():
    print(f"Valor: {valor}")
    

limpio = {clave: valor for clave, valor in sensor.items() if valor is not None}
print("Diccionario limpio:", limpio)



from collections import defaultdict

# defaultdict para agrupar lecturas por sensor
lecturas_por_sensor = defaultdict(list)
lecturas_por_sensor["T1"].append(22.5)
lecturas_por_sensor["T1"].append(22.7)
lecturas_por_sensor["T2"].append(30.1)
print("Lecturas por sensor (defaultdict):", lecturas_por_sensor)


# Si tenemos necesidad de contabilizar palabras dentro de una lista podemos usar counter
from collections import Counter
# Counter para conteo de palabras
texto = ["dato", "sensor", "dato", "embebido", "sensor", "dato"]
conteo = Counter(texto)
print("Conteo de palabras:", conteo) # Nos devuelve un diccionario con el conteo de palabras

print(f"Existe la clave 'temperatura' en el diccionario: {'temperaturas' in sensor}")


# setdefault
config = {}
valor = config.setdefault("modo", "normal") # Como no existe, la crea con el valor 'normal' por defecto
print(f"Valor devuelto: {valor}")
print("Config con setdefault:", config)
    
# Podemos escribirlo de otra forma, pero con setdefult queda más limpio
if "modo" not in config:
    config["modo"] = "normal"