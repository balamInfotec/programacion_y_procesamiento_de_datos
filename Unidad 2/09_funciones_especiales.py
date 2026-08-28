import numpy as np
from scipy.special import jv, erf

# Crear una senal senoidal con ruido
# linspace genera 1000 instantes igualmente espaciados entre 0 y 1 segundo.
t = np.linspace(0, 1, 1000)
# Una semilla fija permite reproducir la misma senal aleatoria en cada ejecucion.
rng = np.random.default_rng(42)
# normal(media, desviacion_estandar, cantidad) genera el ruido gaussiano.
ruido = rng.normal(0, 0.1, 1000)
# La senal combina una onda de 50 Hz con el ruido muestra por muestra.
s = np.sin(2 * np.pi * 50 * t) + ruido
print("Señal original (primeros 10):", s[:10])
# std calcula la dispersion de los valores respecto a su media.
print("Desviación estándar de s:", s.std())
# percentile(s, 95) devuelve el valor por debajo del cual se encuentra el 95 % de los datos.
print("Percentil 95 de s:", np.percentile(s, 95))

# Limitar la amplitud con clip
# np.clip(x, minimo, maximo) hace esto:
#   - si un valor es menor que minimo, lo cambia a minimo
#   - si un valor es mayor que maximo, lo cambia a maximo
#   - si ya esta dentro del rango, lo deja igual
# Ejemplos:
#   np.clip(-1.445, -1, 1) -> -1.0
#   np.clip(1.234, -1, 1)  -> 1.0
#   np.clip(0.5, -1, 1)    -> 0.5
# Es decir, no redondea, solo 'satura' el valor al extremo permitido.
# Es muy útil cuando quieres limitar amplitudes de señales, por ejemplo:
# evitar picos demasiado altos
# asegurar que valores negativos no bajen de un rango
# proteger la señal para que no se salte de cierto rango
limpia = np.clip(s, -1, 1)
# [:10] permite inspeccionar solo las primeras 10 muestras.
print("Señal limitada (primeros 10):", limpia[:10])

# Reemplazar valores NaN usando where
# copy crea una copia para conservar la senal original sin valores faltantes.
s_nan = s.copy()
# [::100] significa 'tomar los elementos en pasos de 100':
#   0, 100, 200, 300, ...
# Es decir, se seleccionan posiciones cada 100 elementos para simular datos faltantes.
# En esas posiciones se reemplaza el valor real por NaN, que significa 'No es un número'.
# Por ejemplo, si s_nan = [x0, x1, x2, ..., x99, x100, ...], entonces:
#   s_nan[0] = NaN, s_nan[100] = NaN, s_nan[200] = NaN, ...
# isnan identifica esos NaN y where los reemplaza por 0.0.
# np.isnan(x): devuelve True donde x es NaN, False en el resto.
#   Ejemplo: np.isnan([1.0, np.nan, 3.0]) -> [False, True, False]
# np.where(condicion, valor_si_verdadero, valor_si_falso):
#   - condicion: arreglo booleano, normalmente el resultado de np.isnan(...)
#   - valor_si_verdadero: valor que se pone donde la condicion es True
#   - valor_si_falso: valor que se pone donde la condicion es False
# En este caso: si un valor es NaN -> poner 0.0; si no lo es -> conservar el valor original.
s_nan[::100] = np.nan
print("Señal con NaN (primeros 10):", s_nan[:10])
s_sin_nan = np.where(np.isnan(s_nan), 0.0, s_nan)
print("Señal con NaN reemplazados (primeros 10):", s_sin_nan[:10])

# Usar funciones especiales de SciPy
# jv(orden, x) calcula la funcion de Bessel de primera especie de orden indicado.
x = np.linspace(0, 10, 100)
bessel = jv(0, x)
# erf calcula la funcion de error, comun en probabilidad y estadistica.
error_f = erf(x / np.sqrt(2))
# Se muestran solo algunos valores para evitar imprimir los arreglos completos.
print("Bessel J0 (primeros 5):", bessel[:5])
print("Función error (primeros 5):", error_f[:5])