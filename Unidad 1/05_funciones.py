def mi_funcion(): # Definiendo una función básica
    print("Mi función")
    
def funcion_suma(numero_uno, numero_dos): # Definiendo una función que recibe 2 parámetros
    resultado = numero_uno + numero_dos # Sumando los parámetros
    print(f"Resultado de la suma {resultado}") # Formateando la salida en consola del resultado
    
def funcion_resta(numero_uno, numero_dos):
    return numero_uno - numero_dos # Función que retorna la resta de los dos parámetros
    
#mi_funcion()
num_uno = int(input("Ingresa el primer número: ")) # Hay que convertir los valores obtenidos por input, porque originalmente son strings
num_dos = int(input("Ingresa el segundo número: "))
print(type(num_uno)) # Utilizamos type para saber el tipo de dato de una variable
funcion_suma(num_uno, num_dos) # Llamada a la función suma

resultado = funcion_resta(12, 2) # Llamada a la función resta, la cual retorna un valor que almacenamos en resultado
print(resultado)