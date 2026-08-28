"""
    Los conjuntos son una estructura de datos que permiten almacenar elementos únicos y no ordenados. 
    En Python, los conjuntos se representan mediante la clase `set`. A continuación, se presentan algunas 
    operaciones básicas que se pueden realizar con conjuntos:
"""
conjunto = {1, 2, 3, 4, 5, 4, 5}

# Agregar un elemento al conjunto
conjunto.add(6)
print(f"Conjunto: {conjunto}")

lista = [1, 1, 3, 5, 5, 6]
# Convertir una lista en un conjunto para eliminar duplicados
conjunto_desde_lista = set(lista)
print(f"Conjunto desde lista: {conjunto_desde_lista}")

# Operaciones de teoría de conjuntos
a = {1, 2, 3}
b = {3, 4, 5}

print("Intersección a & b:", a & b)
print("Unión a | b:", a | b)
print("Diferencia a - b:", a - b)
print("Diferencia simétrica a ^ b:", a ^ b)

etiquetas = {"python", "programación", "conjuntos", "ejemplo"}
print("Etiquetas:", etiquetas)
print(f"Existe python? {'python' in etiquetas}")


numeros = {1, 2, 3, 4, 5}
mayores = set(filter(lambda x : x > 2, numeros))
print(f"Resultado: {mayores}")


