"""
    Las listas son elementos que nos permiten almacenar varios valores en una sola variable.
"""

frutas = ["naranja", "banana", "kiwi", "pera", "manzana"]
print(f"Lista de frutas: {frutas}")

# Podemos acceder por índice a cada uno de los elementos de la lista
print(f"Primera fruta: {frutas[0]}")
print(f"Primera fruta: {frutas[-1]}")  # Accedemos al último elemento de la lista

"""
    Podemos obtener rebanas de una lista de la siguiente manera
"""
print(f"Rebanada de frutas: {frutas[1:3]}")  # Obtenemos los elementos desde el índice 1 hasta el índice 2
print(f"Rebana desde el inicio: {frutas[0:3]}")
print(f"Rebana desde el inicio: {frutas[:3]}")

# Pedemos obtener 'saltos' utilizando un tercer parámetro
print(f"Saltos en la rebanada: {frutas[::2]}")  # Obtenemos los elementos desde el inicio hasta el final con un salto de 2

# Podemos invertir los elementos de una lista
print(f"Lista de frutas: {frutas}")
print(f"Lista invertida: {frutas[::-1]}")  # Obtenemos los elementos desde el final hasta el inicio con un salto de -1

entrada = "Anita lava la tina"
entrada_limpia = entrada.replace(" ", "").lower()  # Eliminamos los espacios y convertimos a minúsculas
print(f"Entrada: {entrada}")
print(f"Entrada limpia: {entrada_limpia}")
# Vamos a crear un programa que identifique si es un palíndromo
print(f"Entrada invertida: {entrada_limpia[::-1]}")
if entrada_limpia == entrada_limpia[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
    
frutas = ["naranja", "banana", "kiwi"]
# Podemos desempaquetar los elementos de un arreglo para almacenarlos en variables
fruta1, fruta2, fruta3 = frutas
print(f"Fruta 1: {fruta1}")
print(f"Fruta 2: {fruta2}")
print(f"Fruta 3: {fruta3}")

# Podemos utilizar un comodín para obtener el resto de elementos
fruta1, *resto_frutas = frutas
print(f"Fruta 1: {fruta1}")
print(f"Resto de frutas: {resto_frutas}")

# Podemos modificar elementos de la lista mediante índice
frutas[2] = "sandía"
print(f"Lista de frutas modificada: {frutas}")

# Podemos utilizar append para agregar elementos al final de la lista
frutas.append("mango")  # Agregamos un elemento al final de la lista
print(f"Lista de frutas con mango: {frutas}")

# Podemos utilizar insert para insertar elementos en ciertas posiciones de nuestra lista
frutas.insert(1, "fresa")  # Insertamos un elemento en la posición 1
print(f"Lista de frutas con fresa: {frutas}") 

verduras = ["zanahoria", "lechuga", "pepino"]
frutas.extend(verduras)  # Agregamos los elementos de la lista verduras al final de la lista frutas
print(f"Lista de frutas y verduras: {frutas}")

lista_numeros = [1, 2, 3, 4, 5]
resultado = lista_numeros * 2

print(f"Lista de números multiplicada por 2: {resultado}")  # Multiplicamos la lista por 2, obteniendo una nueva lista con los elementos repetidos

lista_numeros.reverse()

print(f"Lista de números reservada: {lista_numeros}")  # Mostramos la lista de números reservada

import random
nueva_lista = [random.randint(0, 100) for _ in range(20)]  # Creamos una lista de 10 números aleatorios entre 0 y 100
print(f"Nueva lista de números aleatorios: {nueva_lista}")

nueva_lista = [10, 4, 6, 20, 30, 50, 100]

"""
    FILTRADO
    Puedo utilizar la función filter para obtener elementos que cumplan con ciertos criterios de selección
"""
mayores = list(filter(lambda x: x > 10, nueva_lista))  # Obtenemos los elementos mayores a 10
print(f"Lista original: {nueva_lista}")
print(f"Elementos mayores a 10: {mayores}")

mi_funcion = lambda numero_uno, numero_dos: numero_uno + numero_dos  # Creamos una función lambda que suma dos números

def suma(numero_uno, numero_dos):
    return numero_uno + numero_dos  # Retornamos la suma de los dos números

print(f"Suma de 2 y 3 utilizando la función lambda: {mi_funcion(2, 3)}")


"""
    TRANSFORMACIÓN
    Podemos utilizar la función map para aplicar una función a cada uno de los elementos de una lista
"""
cuadrados = list(map(lambda x: x ** 2, nueva_lista))  # Obtenemos los cuadrados de los elementos
print(f"Cuadrados de los elementos: {cuadrados}")

