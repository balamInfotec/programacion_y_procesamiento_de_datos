"""
    Filtrado básico con scipy
"""
import matplotlib.pyplot as plt
from scipy.signal import medfilt

tiempo = list(range(8))
temperatura_ruidosa = [20, 21, 35, 22, 23, 24, 40, 25]

temperatura_filtrada = medfilt(temperatura_ruidosa, kernel_size=3)
print(f"\nMediciones originales: {temperatura_ruidosa}")
print(f"\nMediciones filtradas: {temperatura_filtrada}")

# Graficando datos
fig, ax = plt.subplots(figsize=(9,4))
ax.plot(
    tiempo,
    temperatura_ruidosa,
    marker="o",
    label="Original"
)
ax.plot(
    tiempo,
    temperatura_filtrada,
    marker="o",
    label="Filtrada"
)

ax.set(
    title="Filtro de mediana",
    xlabel="Tiempo",
    ylabel="Temperatura"
)

ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
plt.show()

