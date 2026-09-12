"""
    Validación estricta de datos
"""

from pydantic import BaseModel
# pip install pydantic

class LecturaAPISinValidacion:
    def leer_datos(self):
        # Implementación de lectura desde la API Open-Meteo
        datos = {
            "temperatura": [25.5, 26.0, 24.8, 23.5, 22.0],
            "humedad": [60, 65, 70, 75, 80],
            #"viento": [10, 12, 8, 15, 20],
            "viento": 12,
        }
        return datos
    
class ImprimirDatosSinValidacion:
    def mostrar_datos(self, datos):
        print(f"Datos procesados:\nTemperatura: {datos['temperatura']}\nHumedad: {datos['humedad']}\nViento: {datos['viento']}")        
        
# Definimos una clase como base para nuestro contrato
class DatosSensores(BaseModel):
    temperatura: list
    humedad: list
    viento: list

class LecturaAPI:
    def leer_datos(self) -> DatosSensores:
        # Implementación de lectura desde la API Open-Meteo
        datos = {
            "temperatura": [25.5, 26.0, 24.8, 23.5, 22.0],
            "humedad": [60, 65, 70, 75, 80],
            "viento": [10, 12, 8, 15, 20],
        }
        # el doble ** permite desempaquetar el diccionario y pasar sus elementos como argumentos de palabra clave al constructor de DatosSensores.
        #return DatosSensores(**datos)
        
        datos = DatosSensores(
            temperatura=[25.5, 26.0, 24.8],
            humedad=[60, 65, 70],
            viento=[10, 12, 8]
            #viento=10
        )
        
        return datos
        
class ImprimirDatos:
    def mostrar_datos(self, datos: DatosSensores):
        print(f"Datos procesados:\nTemperatura: {datos.temperatura}\nHumedad: {datos.humedad}\nViento: {datos.viento}")
        

if __name__ == "__main__":
    # Sin validación estricta
    print("Lectura de datos sin validación estricta:")
    lector_api = LecturaAPISinValidacion()
    datos = lector_api.leer_datos()
    visualizador = ImprimirDatosSinValidacion()
    visualizador.mostrar_datos(datos)

    # Con validación estricta
    print("\nLectura de datos con validación estricta:")
    # Leer desde API Open-Meteo para Ciudad de Mexico
    lector_api = LecturaAPI()
    datos = lector_api.leer_datos()
    
    # Visualizar los datos procesados en la consola
    visualizador = ImprimirDatos()
    visualizador.mostrar_datos(datos)