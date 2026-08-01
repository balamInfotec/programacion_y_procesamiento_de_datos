import math # Funciones de cálculo matemático
import random # Generar números aleatorios

'''
Podemos utilizar las funciones de conversión de datos:
int()
float()
str
'''
opcion = int(input("Ingresa una opción: ")) # Input devuelve una cadena, pero, si esa cadena es un entero, podemos convertirla con int()
numero_cadena = str(22) # Podemos convertir directamente números a cadena, para que ya no sean tratados como números

numero_uno = "5"
numero_dos = 10
#resultado = numero_uno + numero_dos # CUIDADO: Python genera un error, no se pueden sumar cadenas con números
resultado = int(numero_uno) + numero_dos # CORRECTO!, convertimos lo necesario para poder realizar la suma
print(f"Resultado: {resultado}")

resultado = math.sqrt(25) # Calculamos la raíz cuadrada
print(f"Raíz cuadrada: {resultado}")


numero_aleatorio = random.randint(1, 10) # Obtenemos un número aleatorio entre 1 y 10
print(f"Número aleatorio: {numero_aleatorio}")

print(f"Tipo de dato del número aleatorio: {type(numero_aleatorio)}") # Imprimimos con type el tipo de dato correspondiente

