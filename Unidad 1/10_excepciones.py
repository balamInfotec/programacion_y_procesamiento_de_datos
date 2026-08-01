try:
    resultado = 10/0
except: # Excepción genérica, captura todo tipo de error, lo ideal es clarificar qué tipos de errores pueden ocurrir
    print("Error")

try:
    resultado = 10/0 # Esto lanzará una excepción, sino se usa try-except, el programa terminará inesperadamente
except ZeroDivisionError: # Utilizar los tipos de erorr en una excepción para mayor claridad
    print("Error: No puedes dividir entre cero")
    
try:
    numero = int("Hola") # Error intencionado, intentamos convertir una cadena en número entero
except ValueError as e: # Tipo de error definido para capturar, y usamos la variable e para poder acceder al mensaje de error
    print(f"Ocurrió un error: {e}")
    
try:
    resultado = 10/0
except ZeroDivisionError:
    print("División entre cero no permitida")
except TypeError: # Podemos definir distintos tipos de error y personalizar los flujos que se ejecutarán
    print("Tipos de datos incompatibles")
    
try:
    n = int("5")
except ValueError:
    print("Error de conversión")
else: # Se ejecuta solo si no hubo excepción
    print("Conversión existosa:", n)
    
try:
    n = int("hola")
except ValueError:
    print("Error de conversión")
else: # Se ejecuta solo si no hubo excepción
    print("Conversión existosa:", n)
finally:
    print("Se ejecuta siempre, aunque haya excepción")
    
try:
    opcion = 10
    if opcion == 10:
        raise ValueError("Error de valor!!!") # Podemos usar raise para lanzar una excepción
except ValueError as e:
    print(f"Ocurrió la siguiente excepción: {e}")


class ErrorPersonalizado(Exception): # Podemos crear una excepción personalizada, heredando de Exception
    pass

try:
    opcion = 10
    if opcion == 10:
        raise ErrorPersonalizado("Error personalizado!!!") # Podemos usar raise para lanzar una excepción
except ErrorPersonalizado as e:
    print(f"Ocurrió la siguiente excepción: {e}")
    
class OtroError(Exception):
    def __init__(self, servidor, puerto, mensaje): # Podemos agregar más atributos a la excepción
        super().__init__(mensaje) # La clase padre maneja el mensaje de error
        self.servidor = servidor # los atributos los maneja la clase hija
        self.puerto = puerto
        
try:
    opcion = 10
    if opcion == 10:
        raise OtroError("localhost", 21, "Error personalizado!!!") # Podemos usar raise para lanzar una excepción
except OtroError as e:
    print(f"Ocurrió la siguiente excepción: {e} en el servidor: {e.servidor} en el puerto {e.puerto}")