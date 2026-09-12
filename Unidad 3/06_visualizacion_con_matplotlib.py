"""
    Graficación con matplot lib
"""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

ventas = pd.DataFrame(
    {
        "mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
        "ventas": [1200, 1450, 1680, 1550, 1900, 2300],
        "visitas": [80, 95, 110, 105, 125, 150],
    }
)

# Generar una gráfica con salida de archivo
carpeta_salida = Path(__file__).parent / "06_visualizacion_matplotlib"
# Creamos la carpeta y en caso de que no exista, se evita un error
carpeta_salida.mkdir(exist_ok=True)

# Crear la gráfica
figura, ax = plt.subplots(figsize=(8,4))
ax.plot(ventas["mes"], ventas["ventas"], marker="o", color="navy")
ax.set_title("Ventas mensuales")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas ($)")
# con grid podemos especificar una cuadrícula en el fondo de la gráfica
# utilizando el parámetro alpha definimos la transparencia de la cuadrícula
ax.grid(alpha=0.3)
# tight_layout ajusta automáticamente los márgenes de la figura
figura.tight_layout()

# Generamos el archivo de salida como png, en la carpeta correspondiente
figura.savefig(carpeta_salida / "01_visualizacion_grafica.png", dpi=150)
plt.close(figura)




# Grafica de barras: util para comparar categorias.
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(ventas["mes"], ventas["ventas"], color="darkorange")
ax.set_title("Comparacion de ventas por mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas ($)")
fig.tight_layout()
fig.savefig(carpeta_salida / "08_barras_ventas.png", dpi=150)
plt.close(fig)

# Grafica de dispersion: permite observar la relacion entre dos variables.
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(ventas["visitas"], ventas["ventas"], color="seagreen", s=80)
ax.set_title("Relacion entre visitas y ventas")
ax.set_xlabel("Visitas")
ax.set_ylabel("Ventas ($)")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(carpeta_salida / "08_dispersion_visitas_ventas.png", dpi=150)
plt.close(fig)

# Histograma: muestra la distribucion de un conjunto de valores.
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(ventas["ventas"], bins=4, color="mediumpurple", edgecolor="white")
ax.set_title("Distribucion de las ventas")
ax.set_xlabel("Ventas ($)")
ax.set_ylabel("Frecuencia")
fig.tight_layout()
fig.savefig(carpeta_salida / "08_histograma_ventas.png", dpi=150)
plt.close(fig)

print(f"Se guardaron cuatro graficas en: {carpeta_salida}")