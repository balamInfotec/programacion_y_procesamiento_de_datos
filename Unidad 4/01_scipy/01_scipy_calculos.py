""" 
Cálculos científicos con
SCIPY 

pip install scipy

"""

from scipy.integrate import quad
from scipy.interpolate import interp1d
from scipy.optimize import brentq, minimize_scalar

print("\nEjemplo 1: calcular el consumo de un dispositivo")

""""
    Ejemplo 1: El dispositivo consume 100mA al inicio, y cada segundo
    aumenta su consumo en 10mA
"""
def corriente(tiempo: float) -> float:
    return 100 + 10 * tiempo

# Calculamos la integral de la función especificada
carga_consumida, error_estimado = quad(corriente, 0, 10)
carga_mAh = carga_consumida / 3600

print(f"Carga consumida: {carga_consumida:.1f} y carga en mA*s: {carga_mAh}")
print(f"El error estimado: {error_estimado}")

"""
    Ejemplo 2: Interpolación
"""
print(f"\nEjemplo 2: Interpolación")

horas = [8, 10, 12, 14]
temperaturas = [18, 22, 27, 25]

interpolador = interp1d(
    horas,
    temperaturas,
    kind="linear",
    fill_value="extrapolate"
)

hora_consultada = 11

print(f"\nTemperatura estimada a las {hora_consultada}: {float(interpolador(hora_consultada))}")


"""
    Ejemplo 3: Buscar un mínimo dada una función
"""

print(f"\nEjemplo 3: Buscar un mínimo dada una función")

# Costo aproximado de operar una máquina a cierta temperatura
def costo_aproximado(temperatura: float) -> float:
    return (temperatura - 22)**2 + 10

resultado = minimize_scalar(
    costo_aproximado,
    bounds=(15, 30),
    method="bounded"
)

if not resultado.success:
    # En caso de error
    raise RuntimeError(f"No se pudo encontrar el mínimo: {resultado.message}")

print(f"\nTemperatura recomendada: {resultado.x:.1f} grados")
print(f"\nCosto mínimo: {resultado.fun:.1f}")


"""

    Ejemplo 4: Cálculo de raíz

"""
print(f"Ejemplo 4: Cálculo de raíz")

def diferencia_temperatura(valor: float) -> float:
    return valor - 25

temperatura_objetivo = brentq(
    diferencia_temperatura,
    20,
    30
)

print(f"Temperatura que iguala la meta: {temperatura_objetivo:.1f} grados")

