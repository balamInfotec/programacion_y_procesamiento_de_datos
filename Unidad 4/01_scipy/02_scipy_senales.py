"""
    Tratamiento de señales con SCIPY
"""

import matplotlib.pyplot as plt
from scipy.signal import find_peaks

tiempo = list(range(10))
temperatura = [20, 21, 24, 22, 23, 27, 25, 24, 28, 26]

# height indica que solos queremos picos con valor de 23 o mayor
indices_picos, propiedades = find_peaks(temperatura, height=23)
print(f"\nÍndice picos: {indices_picos}")
print(f"\nPropiedades: {propiedades}")

for indice, valor in zip(indices_picos, propiedades["peak_heights"]):
    print(f"-minuto {tiempo[indice]}: {valor} grados")

# Graficar
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(tiempo, temperatura, marker="o")
ax.scatter(
    indices_picos,
    [temperatura[i] for i in indices_picos],
    color="red",
    s=100,
    zorder=3,
    label="Picos detectados"
)
ax.set(title="Detección de picos", xlabel="Minuto", ylabel="Temperatura")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
plt.show()




