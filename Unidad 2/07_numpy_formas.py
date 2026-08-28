import numpy as np

# Crear una matriz de 3 filas y 4 columnas
# arange genera los valores del 0 al 11 y reshape cambia su forma a (3, 4).
X = np.arange(12).reshape(3, 4)
print("X:\n", X)
# shape muestra el tamano de cada dimension y ndim indica cuantas dimensiones tiene X.
print("shape:", X.shape, "ndim:", X.ndim)

# Reducciones por eje
# axis=0 recorre las filas y produce una media para cada columna.
# Formula de la media: media = (sumatoria de los valores) / cantidad de valores
# Para la primera columna de X = [0, 4, 8], la media es (0 + 4 + 8) / 3 = 4.0
# Y eso es exactamente lo que vemos en la salida: [ 4.  5.  6.  7. ]
print("Media por columna (axis=0):", X.mean(axis=0))
# axis=1 recorre las columnas y produce una suma para cada fila.
# Por ejemplo, la primera fila es [0, 1, 2, 3], cuya suma es 6.
# La segunda fila es [4, 5, 6, 7], cuya suma es 22.
# La tercera fila es [8, 9, 10, 11], cuya suma es 38.
# La salida sin keepdims seria: [ 6 22 38]
# Con keepdims=True se conserva la dimension reducida como (3, 1):
# [[ 6], [22], [38]]
# Esto es util cuando despues queremos combinar esa salida con otra matriz
# sin perder la estructura de filas y columnas.
print("Suma por fila (axis=1, keepdims=True):\n", X.sum(axis=1, keepdims=True))

# Normalizacion por columna
# La idea es convertir cada columna para que tenga media 0 y desviacion estandar 1.
# Formula general: z = (x - media) / desviacion_estandar
# En este ejemplo, cada columna se normaliza por separado.
# Ejemplo de la primera columna de X: [0, 4, 8]
# media = (0 + 4 + 8) / 3 = 4
# desviacion estandar (aprox.) = 3.266
# Entonces los valores normalizados son:
# (0 - 4) / 3.266 = -1.2247
# (4 - 4) / 3.266 = 0
# (8 - 4) / 3.266 = 1.2247
# Es decir, la columna queda centrada en 0 y escalada para que sus valores
# queden en una escala comparable con las otras columnas.
# NumPy aplica estas operaciones a cada columna mediante broadcasting (sin bucles):
# X.mean(axis=0) devuelve un vector con la media de cada columna.
# X.std(axis=0) devuelve un vector con la desviacion estandar de cada columna.
# Luego NumPy resta y divide cada fila con ese vector, sin necesidad de escribir bucles.
Xn = (X - X.mean(axis=0)) / X.std(axis=0)
print("X normalizada por columna:\n", Xn)

# Broadcasting con un vector
# NO es un slice tipo lista[1:4:2].
# En NumPy, ':' significa 'todas las posiciones de ese eje'.
# 'None' significa 'agrega una nueva dimension con tamaño 1'.
# Entonces:
# arr[fila, columna] eso significa en numpy
#   v[:, None] = toma todos los elementos de v y los pone como columna -> [[1], [2], [3]]  (shape (3, 1))
#   v[None, :] = toma todos los elementos de v y los pone como fila    -> [[1, 2, 3]]     (shape (1, 3))
# Cuando se suman, NumPy expande ambas formas para que coincidan:
#   (3, 1) + (1, 3) -> (3, 3)
# Por eso cada elemento de la matriz resultante es la suma de una fila + una columna.
# Ejemplo: 1 + 1 = 2, 1 + 2 = 3, 1 + 3 = 4, ...
v = np.array([1, 2, 3])
como_columna = v[:, None]
como_fila = v[None, :]
print(f"Transformación a columna:\n{como_columna}\nshape: {como_columna.shape}")
print(f"Transformación a fila:\n{como_fila}\nshape: {como_fila.shape}")
resultado = como_columna + como_fila
print("Matriz generada por broadcasting:\n", resultado)

# Combinar arreglos horizontal y verticalmente
# hstack une arreglos lado a lado, agregando columnas.
# Requiere que los arreglos tengan la misma cantidad de filas.
# En este ejemplo, A y B tienen forma (2, 2), por lo que la salida
# tiene forma (2, 4): 2 filas y 4 columnas.
# Visualmente:
# A = [[1, 1],
#      [1, 1]]
# B = [[0, 0],
#      [0, 0]]
# hstack([A, B]) = [[1, 1, 0, 0],
#                   [1, 1, 0, 0]]
A = np.ones((2, 2))
B = np.zeros((2, 2))
print(f"A:\n{A}\nshape: {A.shape}")
print(f"B:\n{B}\nshape: {B.shape}")
C_h = np.hstack([A, B])
# vstack apila los arreglos uno encima del otro, agregando filas.
# Requiere que los arreglos tengan la misma cantidad de columnas.
# En este ejemplo, ambos tienen forma (2, 2), por lo que la salida
# tiene forma (4, 2): 4 filas y 2 columnas.
# Visualmente:
# A -> dos filas de unos
# B -> dos filas de ceros
# vstack([A, B]) = [[1, 1],
#                   [1, 1],
#                   [0, 0],
#                   [0, 0]]
C_v = np.vstack([A, B])
print("hstack:\n", C_h)
print("vstack:\n", C_v)

