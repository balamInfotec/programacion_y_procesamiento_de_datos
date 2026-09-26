from scipy import ndimage
import imageio.v3 as iio
import numpy as np

# Cargar imágenes
imagen_uno = iio.imread("movimiento1.png")
imagen_dos = iio.imread("movimiento2.png")

# Convertir a escala de grises
escala_grises_uno = np.mean(imagen_uno, axis=2)
escala_grises_dos = np.mean(imagen_dos, axis=2)

# Las imágenes tienen tamaños distintos, por lo que no se pueden restar
# directamente. Se conserva la zona común de ambas usando la menor altura
# y el menor ancho, sin deformar las imágenes mediante un redimensionamiento.
alto = min(escala_grises_uno.shape[0], escala_grises_dos.shape[0])
ancho = min(escala_grises_uno.shape[1], escala_grises_dos.shape[1])
escala_grises_uno = escala_grises_uno[:alto, :ancho]
escala_grises_dos = escala_grises_dos[:alto, :ancho]

# Bordes
bordes_uno = ndimage.sobel(escala_grises_uno)
bordes_dos = ndimage.sobel(escala_grises_dos)

# Diferencia de movimiento
# Resta la intensidad de cada borde de la primera imagen a la de la segunda.
# np.abs() convierte las diferencias negativas en positivas, porque interesa
# medir cuánto cambió el borde sin importar la dirección del cambio.
# La condición "> 40" crea una máscara booleana: True cuando el cambio es
# mayor que 40 y False cuando es igual o menor. El valor 40 es un umbral
# práctico para ignorar pequeñas variaciones producidas por ruido, iluminación
# o compresión de la imagen; no es un valor universal y puede ajustarse según
# las imágenes y la sensibilidad de movimiento que se necesite.
# np.sum() cuenta los valores True (cada uno equivale a 1), produciendo la
# cantidad de píxeles cuyos bordes cambiaron significativamente.
resultado = np.sum(np.abs(bordes_dos - bordes_uno) > 40)

print("Nivel de movimiento:", resultado)