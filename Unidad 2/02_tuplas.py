"""
    Las tuplas son secuencias ordenadas de elementos, similares a las listas, pero con la diferencia de que son inmutables. 
    Esto significa que una vez creada una tupla, no se pueden modificar sus elementos (no se pueden agregar, eliminar 
    o cambiar elementos).
"""
sensor = ("T1", 23.5, 45.2, True)
configuracion = (3304, 0.5, "activo")

print(f"Accediendo al primer elemento de la tupla sensor: {sensor[0]}")
print(f"Accediendo al último elemento de la tupla sensor: {sensor[-1]}")

# Podemos utilizar rebanadas para obtener información
print(f"Rebanada de información: {sensor[0:2]}")
print(f"Invertir la tupla: {sensor[::-1]}")

# Desempaque de información
nombre, temperatura, humedad, estado = sensor
print(f"Nombre: {nombre}, Temperatura: {temperatura}, Humedad: {humedad}, Estado: {estado}")
nombre, *resto = sensor
nueva_tupla = tuple(resto)
print(f"Tipo de dato del resto: {type(resto)}")
print(f"Tipo de dato del resto: {type(nueva_tupla)}")
print(f"Nombre: {nombre}, Resto de la información: {nueva_tupla}")

tupla = (5,)
print(f"Tipo de dato de la tupla: {type(tupla)}")

tupla_vacia = ()
tupla_vacia = tuple()

print(f"Tipo de dato de la tupla vacía: {type(tupla_vacia)}")

tupla_vacia = tupla_vacia + (5,)
tupla_vacia = tupla_vacia + (10,)
print(f"Tipo de dato de la tupla actualizada: {type(tupla_vacia)}")
print(f"Tupla: {tupla_vacia}")


from collections import namedtuple

Sensor = namedtuple("Sensor", ["nombre", "temperatura", "humedad", "estado"])
sensor_named = Sensor(22, 23.5, 45.2, True)
print(f"Accediendo al primer elemento de la tupla sensor_named: {sensor_named.nombre}")



from dataclasses import dataclass

@dataclass(frozen=True)
class SensorData:
    nombre: str
    temperatura: float
    humedad: float
    estado: bool
    
    def __post_init__(self):
        if not isinstance(self.nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(self.temperatura, (int, float)):
            raise TypeError("La temperatura debe ser un número.")
        if not isinstance(self.humedad, (int, float)):
            raise TypeError("La humedad debe ser un número.")
        if not isinstance(self.estado, bool):
            raise TypeError("El estado debe ser un valor booleano.")

try:
    sensor_data = SensorData(12, 23.5, 45.2, True)
    print(f"Accediendo al primer elemento de la tupla sensor_data: {sensor_data.nombre}")
except TypeError as e:
    print(f"Error al crear SensorData: {e}")
    
    


