"""
Ejemplo 7: comparar ejecución secuencial, hilos y procesos con una carga de CPU grande.

Cada trabajador hace la misma cantidad de cálculos independientes. Con varios
núcleos disponibles, los procesos pueden repartir la carga y superar al hilo
principal y, en Python convencional, a los hilos limitados por el GIL.

Instalación: no se requieren paquetes externos; solo se usa la biblioteca
estándar de Python, así que no hace falta ejecutar pip install.
"""

import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import perf_counter


CANTIDAD = 162_000_000  # Aumenta la carga para que el cálculo compense el costo de crear procesos.


def calcular_bloque(inicio, fin):
    """Realiza cálculos enteros de CPU para los valores de [inicio, fin)."""
    total = 0

    # Cada iteración hace trabajo independiente y no depende de datos compartidos.
    for numero in range(inicio, fin):
        total += (numero * numero) % 97

    return total


def medir(nombre, funcion):
    """Mide el tiempo total hasta que la estrategia devuelve su resultado."""
    inicio = perf_counter()  # Usa un reloj monotónico para medir duración transcurrida.
    resultado = funcion()  # En las estrategias paralelas, esta llamada espera a que terminen sus tareas.
    duracion = perf_counter() - inicio
    print(f"{nombre}: {duracion:.3f} s")
    return resultado


def dividir_en_bloques(cantidad, trabajadores):
    """Divide el intervalo en bloques casi iguales para equilibrar el trabajo."""
    tamano_bloque = (cantidad + trabajadores - 1) // trabajadores

    # El extremo final se limita a cantidad para no procesar valores de más.
    return [
        (inicio, min(inicio + tamano_bloque, cantidad))
        for inicio in range(0, cantidad, tamano_bloque)
    ]


def calcular_secuencial(bloques):
    """Procesa los mismos bloques uno tras otro para tener una referencia."""
    return sum(calcular_bloque(inicio, fin) for inicio, fin in bloques)


def calcular_con_hilos(bloques, trabajadores):
    """Envía cada bloque a un grupo de hilos y suma sus resultados."""
    with ThreadPoolExecutor(max_workers=trabajadores) as executor:
        # map() programa el mismo cálculo para cada bloque y entrega cada resultado al terminar.
        resultados = executor.map(calcular_bloque, (inicio for inicio, _ in bloques), (fin for _, fin in bloques))
        return sum(resultados)


def calcular_con_procesos(bloques, trabajadores):
    """Envía cada bloque a un grupo de procesos independientes."""
    with ProcessPoolExecutor(max_workers=trabajadores) as executor:
        # map() distribuye las llamadas entre procesos y propaga los errores al consultar resultados.
        resultados = executor.map(calcular_bloque, (inicio for inicio, _ in bloques), (fin for _, fin in bloques))
        return sum(resultados)


def main():
    # Limitar los trabajadores hace manejable el ejemplo en equipos con muchos núcleos.
    trabajadores = min(os.cpu_count() or 1, 4)
    bloques = dividir_en_bloques(CANTIDAD, trabajadores)
    print(f"CPU disponibles: {os.cpu_count() or 1}") # 8
    print(f"Trabajadores: {trabajadores}") # 4
    print(f"Bloques de trabajo: {bloques}") # [(0, 8000000), (8000000, 16000000), (16000000, 24000000), (24000000, 32000000)]

    # Cada estrategia recibe exactamente los mismos intervalos para comparar resultados equivalentes.
    resultado_secuencial = medir(
        "Secuencial",
        lambda: calcular_secuencial(bloques),
    )
    resultado_hilos = medir(
        "Hilos",
        lambda: calcular_con_hilos(bloques, trabajadores),
    )
    resultado_procesos = medir(
        "Procesos",
        lambda: calcular_con_procesos(bloques, trabajadores),
    )

    # Comprobar la igualdad evita aceptar una comparación si alguna estrategia omitió trabajo.
    if not (resultado_secuencial == resultado_hilos == resultado_procesos):
        raise RuntimeError("Los resultados no coinciden; revisa la distribución de bloques.")

    print(f"Resultado común: {resultado_secuencial}")
    print(f"Bloques: {len(bloques)}; trabajadores: {trabajadores}")
    print("Los procesos suelen aventajar en esta carga de CPU si hay varios núcleos disponibles.")


if __name__ == "__main__":
    # Es obligatorio en Windows: evita crear procesos hijos al importar este archivo.
    main()
