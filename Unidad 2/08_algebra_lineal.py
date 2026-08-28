import numpy as np

# Resolver un sistema lineal de la forma A x = b
# A contiene los coeficientes del sistema, b contiene los resultados conocidos
# y x es la solución que queremos encontrar.
# Por ejemplo:
#   2x + y = 5
#   x + 3y = 10
# En NumPy, np.linalg.solve(A, b) resuelve esto directamente sin invertir A a mano.
A = np.array([[2., 1.],
              [1., 3.]])
b = np.array([5., 10.])

x = np.linalg.solve(A, b)
print("Solución del sistema:", x)
# @ es el operador de multiplicacion de matrices en NumPy.
# No es un operador de Python general para listas, sino que NumPy lo sobrecarga
# para arreglos de tipo array.
# A @ x significa: 'multiplicar la matriz A por el vector x'.
# En este caso, A es 2x2 y x es un vector de longitud 2.
# El resultado debe coincidir exactamente con b:
#   A @ x = [2*x1 + x2, x1 + 3*x2]
# y para la solución encontrada, ese resultado debe ser [5, 10].
# Es equivalente a escribir np.matmul(A, x).
# Ambas formas producen el mismo resultado: multiplicar la matriz A por el vector x.
# Esto sirve para verificar que la solución hallada realmente cumple la ecuación.
print("Comprobación: A @ x =", A @ x)
print("Comprobación con np.matmul(A, x):", np.matmul(A, x))

# Calcular el determinante y el número de condición
# El determinante ayuda a saber si la matriz es invertible.
# Si det(A) == 0, la matriz es singular y no puede resolverse como un sistema estándar.
detA = np.linalg.det(A)
# El número de condición mide qué tan sensible es la solución a pequeños cambios en los datos.
# Un valor cercano a 1 indica buena estabilidad; valores grandes indican mayor riesgo de inestabilidad.
condA = np.linalg.cond(A)
print("Determinante de A:", detA)
print("Número de condición de A:", condA)

# Ajuste por mínimos cuadrados
# En muchos casos no existe una solución exacta para y = M * coef,
# por eso se busca la recta o modelo que minimiza el error cuadrático.
# Cada fila de M representa una observación:
#   [x, 1]
# y cada valor de y es la salida observada.
# Queremos encontrar coeficientes c0 y c1 tal que:
#   y ≈ c0 * x + c1
# Es decir, ajustar una línea a los puntos.
M = np.array([[0., 1.],
              [1., 1.],
              [2., 1.],
              [3., 1.]])
y = np.array([1., 2., 2., 3.])

# np.linalg.lstsq busca los coeficientes que minimizan el error cuadrático.
# Firma: np.linalg.lstsq(a, b, rcond=None)
#   a: matriz de diseño (cada fila es una observación, cada columna un coeficiente del modelo)
#   b: vector con los valores observados que se intentan aproximar
#   rcond: controla el tratamiento de valores singulares; None usa el valor por defecto
# Los resultados normalmente incluyen: coeficientes, residuos, rango, etc.
# El operador *_ ignora los valores adicionales que devuelve la función y solo guarda los coeficientes.
coef, *_ = np.linalg.lstsq(M, y, rcond=None)
print("Coeficientes por mínimos cuadrados:", coef)
# En este ejemplo, coef representa la recta que mejor aproxima los datos.
# Si la ecuación es y ≈ a*x + b, entonces coef[0] sería a y coef[1] sería b.

