import numpy as np
from scipy import ndimage
# pip install imageio
import imageio.v3 as iio
import matplotlib.pyplot as plt

# 1. Cargar imagen
imagen = iio.imread("imagen.jpg")  # Usa cualquier imagen
imagen_escala_grises = np.mean(imagen, axis=2)      # Convertir a escala de grises

# 2. Filtro de bordes (Sobel)
# Aplica el filtro de Sobel en el eje vertical (filas). Detecta cambios
# de intensidad entre píxeles situados arriba y abajo; por eso resalta
# principalmente los bordes horizontales.
filtro_x = ndimage.sobel(imagen_escala_grises, axis=0)

# Aplica el filtro de Sobel en el eje horizontal (columnas). Detecta cambios
# de intensidad entre píxeles situados a la izquierda y a la derecha; por eso
# resalta principalmente los bordes verticales.
filtro_y = ndimage.sobel(imagen_escala_grises, axis=1)

# Combina las dos respuestas del filtro de Sobel calculando su magnitud:
# sqrt(sx**2 + sy**2). np.hypot() realiza este cálculo de forma segura
# y produce la intensidad total del borde en cada píxel.
bordes = np.hypot(filtro_x, filtro_y)

plt.imshow(bordes, cmap="gray")
plt.title("Bordes detectados")
plt.axis("off")
plt.show()
