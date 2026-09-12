import pandas as pd
from abc import ABC, abstractmethod
from urllib.parse import urlencode
from urllib.request import urlopen
import json

"""
    1. Principio de Responsabilidad Única (SRP)
    Cada clase tiene una única responsabilidad y razón para cambiar.
    
    2. Principio de Abierto/Cerrado (OCP)
    Las clases están abiertas para la extensión pero cerradas para la modificación.
    
    3. Principio de Sustitución de Liskov (LSP)
    Las subclases deben ser sustituibles por sus clases base sin alterar el comportamiento esperado.
    
    4. Principio de Segregación de Interfaces (ISP)
    Las interfaces deben ser específicas y no obligar a las clases a implementar métodos que no necesitan
    
    5. Principio de Inversión de Dependencias (DIP)
    Las clases de alto nivel no deben depender de clases de bajo nivel, sino de abstracciones
"""

# Interfaz que define el contrato
class LecturaSensores(ABC):
    @abstractmethod
    def leer_datos(self) -> pd.DataFrame:
        pass
    
class LecturaCSV(LecturaSensores):
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        
    def leer_datos(self) -> pd.DataFrame:
        return pd.read_csv(
            self.ruta_csv,
            sep=",",
            encoding="utf-8"
        )
        
class LecturaSQL(LecturaSensores):
    def __init__(self, conexion_sql):
        self.conexion_sql = conexion_sql
        
    def leer_datos(self) -> pd.DataFrame:
        # Implementación de lectura a la BD Oracle
        datos = {
            "producto": ["Cuaderno", "Pluma", "Mochila", "Termo", "Lapiz"],
            "categoria": ["Papeleria","Papeleria","Accesorios","Accesorios","Papeleria"],
            "precio": [45.50, 12.00, 380.00, 250.00, 8.50],
            "existencias": [20, 80, 12, 15, 100],
        }
        
        return pd.DataFrame(datos)
        
class LecturaAPI(LecturaSensores):
    def __init__(self, latitud, longitud, url_api):
        self.latitud = latitud
        self.longitud = longitud
        self.url_api = url_api

    def leer_datos(self) -> pd.DataFrame:
        # Los parametros se convierten en la cadena de consulta de la URL.
        parametros = {
            "latitude": self.latitud,
            "longitude": self.longitud,
            # Variables meteorologicas que solicitaremos por hora.
            "hourly": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "precipitation,"
                "wind_speed_10m"
            ),
            # Cantidad de dias de pronostico que devolvera el endpoint.
            "forecast_days": 3,
            # Zona horaria usada para que las horas correspondan a Mexico.
            "timezone": "America/Mexico_City",
        }
        # urlencode escapa correctamente los parametros para formar una URL valida.
        url = self.url_api + urlencode(parametros)

        # urlopen realiza la solicitud HTTP; timeout evita esperar indefinidamente.
        # La respuesta se decodifica de bytes a texto y despues de JSON a diccionario.
        with urlopen(url, timeout=30) as respuesta:
            datos_clima = json.load(respuesta)
            
        # La respuesta contiene las variables dentro de la clave "hourly".
        datos_por_hora = datos_clima["hourly"]

        # DataFrame organiza cada hora como una fila y cada variable como una columna.
        return pd.DataFrame(datos_por_hora)
        
        
# Interfaz que define el contrato
class VisualizadorDatos(ABC):
    @abstractmethod
    def mostrar_datos(self, datos: pd.DataFrame):
        pass
    
class VisualizadorPorConsola(VisualizadorDatos):
    def mostrar_datos(self, datos: pd.DataFrame):
        print(f"\nDatos:\n{datos}")
        
class VisualizarHTML(VisualizadorDatos):
    def mostrar_datos(self, datos):
        datos.to_html("07_principios_solid_csv.html")
        
class VisualizarGrafico(VisualizadorDatos):
    def mostrar_datos(self, datos: pd.DataFrame):
        import matplotlib.pyplot as plt
        # Graficar la primera columna contra la segunda
        plt.figure(figsize=(10, 6))
        # todas las filas de la primera columna (datos.iloc[:, 0]) y todas las filas de la tercera columna (datos.iloc[:, 2])
        plt.plot(datos.iloc[:, 0], datos.iloc[:, 2], marker='o')
        plt.title("Gráfico de Datos")
        # columns es una propiedad del DataFrame que devuelve los nombres de las columnas en orden.
        plt.xlabel(datos.columns[0])
        plt.ylabel(datos.columns[2])
        plt.grid()
        plt.show()
        
class Ejecutar:
    def __init__(self, lector: LecturaSensores, visualizador: VisualizadorDatos):
        self.lector = lector
        self.visualizador = visualizador
        
    def ejecutar(self):
        datos = self.lector.leer_datos() # Siempre debe devolver un dataframe
        self.visualizador.mostrar_datos(datos) # Siempre debe recibir un dataFrame
    
if __name__ == "__main__":
    # leer la información a través de un archivo CSV
    lector_csv = LecturaCSV("07_principios_solid.csv")
    lector_base_datos = LecturaSQL("mysql:8300..")
    lector_api = LecturaAPI(
        latitud=19.4326,
        longitud=-99.1332,
        url_api="https://api.open-meteo.com/v1/forecast?"
    )
    
    visualizador_por_consola = VisualizadorPorConsola()
    
    # Visualizar los datos procesados en un archivo HTML
    visualizador_html = VisualizarHTML()
    # Visualizar los datos procesados en un gráfico
    visualizador_grafico = VisualizarGrafico()
    
    obj_ejecutar = Ejecutar(lector=lector_api, visualizador=visualizador_html)
    obj_ejecutar.ejecutar()