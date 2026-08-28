import numpy as np

# NumPy permite trabajar con arreglos numericos de forma eficiente.
# A diferencia de una lista, un arreglo de NumPy tiene una estructura y un tipo
# de dato definidos, lo que facilita las operaciones matematicas.

# Crear un arreglo a partir de una lista
lecturas = [22.5, 23.1, 22.5, 24.0]
print(f"Lista: {lecturas}")
# array convierte la lista en un arreglo de NumPy.
# dtype indica el tipo de dato que tendran todos sus elementos.
# dtype no es necesario si todos los elementos son del mismo tipo; 
# NumPy lo infiere automaticamente.
a = np.array(lecturas, dtype=np.float32)
print("Arreglo 1D:", a)
# shape indica el tamano de cada dimension; ndim, el numero de dimensiones.
# dtype muestra el tipo de dato almacenado y size, la cantidad total de elementos.
# En un arreglo 1D: shape es (n,), porque solo tiene una dimension.
# Es decir, una sola fila con n elementos.
print("shape:", a.shape, "ndim:", a.ndim, "dtype:", a.dtype, "size:", a.size)


# Crear arreglos inicializados con zeros, ones y full
# zeros crea un arreglo lleno de ceros con la forma indicada.
z = np.zeros((3, 3), dtype=np.float32)
# ones crea un arreglo lleno de unos; en este caso tiene 2 filas y 4 columnas.
o = np.ones((2, 4), dtype=np.float32)

print("Arreglo de ceros:\n", z)
print("Arreglo de unos:\n", o)


# Generar secuencias con arange y linspace
# arange inicia en 0, avanza de 2 en 2 y se detiene antes de llegar a 10.
r = np.arange(0, 10, 2)
# linspace genera 5 valores igualmente espaciados entre 0 y 1, incluidos ambos extremos.
l = np.linspace(0, 1, 5)
print("arange:", r)
print("linspace:", l)
