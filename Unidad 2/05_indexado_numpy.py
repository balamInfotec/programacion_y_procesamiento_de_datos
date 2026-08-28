import numpy as np

# Crear una matriz de 3 filas y 4 columnas para practicar indexamiento.
# np.arange(n) genera una secuencia de enteros desde 0 hasta n-1.
# En este caso, arange(12) crea: [0, 1, 2, ..., 11]
# Luego reshape(3, 4) reorganiza esos 12 elementos en 3 filas y 4 columnas.
# Esto es útil para construir matrices de prueba de forma rápida.
X = np.arange(12).reshape(3, 4)
print("X:\n", X)

# Indexado por elemento
# X[fila, columna] permite acceder a un elemento específico.
# Los indices comienzan en cero: [1, 2] selecciona la segunda fila y tercera columna.
print("X[1, 2]:", X[1, 2])

# Seleccionar una columna y una fila completas
# : significa "todas las posiciones" de esa dimension.
print("Primera columna X[:, 0]:", X[:, 0])
print("Primera fila X[0]:", X[0])


# Rebanadas: normalmente producen una vista del arreglo original
# La vista comparte datos con X, aunque representa solo una parte de la matriz.
# Para X =
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# la expresión X[0:2, 1:3] toma:
# - filas desde 0 hasta 1 (2 filas: 0 y 1)
# - columnas desde 1 hasta 2 (2 columnas: 1 y 2)
# Resultado:
# [[1 2]
#  [5 6]]
sub = X[0:2, 1:3]
print("Submatriz (vista):\n", sub)

# Modificar la vista tambien modifica el arreglo original
# Como sub comparte memoria con X, este cambio se refleja en ambos arreglos.
sub[0, 0] = 999
print("Submodificada:\n", sub)
print("X después de modificar sub:\n", X)


# El indexado booleano X[mask] toma solo los valores donde la mascara es True.
# Es decir, devuelve una copia con todos los elementos mayores que 5.
mask = X > 5
picos = X[mask]
print("Elementos > 5 (copia):", picos)


