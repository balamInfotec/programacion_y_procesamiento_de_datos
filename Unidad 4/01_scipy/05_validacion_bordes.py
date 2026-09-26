# Importa ndimage, el módulo de SciPy que contiene funciones para
# procesar imágenes y matrices, entre ellas el filtro de Sobel.
from scipy import ndimage

# Importa la versión 3 de ImageIO y le asigna el alias "iio".
# Se utiliza para leer la imagen desde el archivo.
# pip install imageio
import imageio.v3 as iio

# Importa NumPy para realizar operaciones matemáticas sobre los arreglos
# que representan los píxeles de la imagen.
import numpy as np

# Lee el archivo "imagen2.jpg" y lo convierte en un arreglo de NumPy.
# En una imagen RGB, cada píxel tiene tres valores: rojo, verde y azul.
# La ruta es relativa a la carpeta desde la que se ejecuta el programa.
imagen = iio.imread("imagen.jpg")

# Calcula el promedio de los tres canales de color de cada píxel para
# obtener una imagen en escala de grises.
# axis=2 indica que el promedio se calcula sobre la tercera dimensión
# del arreglo: los canales de color RGB. Así, cada píxel queda representado
# por un solo valor de intensidad en lugar de tres.
escala_grises = np.mean(imagen, axis=2)

# Aplica el filtro de Sobel sobre la imagen en escala de grises.
# Este filtro calcula cambios de intensidad entre píxeles vecinos, que suelen
# corresponder a bordes. No se indica "axis", por lo que SciPy usa su valor
# predeterminado (-1), es decir, la última dimensión disponible.
# Tampoco se indica "mode", por lo que se usa el tratamiento predeterminado
# de los límites de la imagen ("reflect").
bordes = ndimage.sobel(escala_grises)

# Compara cada valor calculado por Sobel con 50 y produce valores booleanos:
# True cuando el valor es mayor que 50 y False en los demás casos.
# El valor 50 es un umbral elegido para considerar suficientemente marcado
# un cambio de intensidad; cambiarlo modifica cuántos puntos se consideran
# bordes.
# np.sum convierte los True en 1 y los False en 0, por lo que cuenta cuántos
# valores superan el umbral.
contador_bordes = np.sum(bordes > 50)

# Muestra en la consola el texto descriptivo y la cantidad de valores que
# superaron el umbral de 50.
print("Bordes detectados:", contador_bordes)