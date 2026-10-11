"""
Ejemplo 6: comparar hilos y procesos con la misma tarea limitada por CPU.

Las mediciones dependen del equipo y de otros programas; este ejemplo sirve
para observar tendencias, no para prometer que una opción siempre será más rápida.

Instalación: no se requieren paquetes externos; solo se usa la biblioteca
estándar de Python, así que no hace falta ejecutar pip install.
"""

import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import perf_counter
from time import sleep


CANTIDAD = 1_000_000  # El total se divide en partes y cada una suma cuadrados.


def sumar_cuadrados(inicio, fin):
    """Suma los cuadrados de los enteros en el intervalo [inicio, fin)."""
    return sum(numero * numero for numero in range(inicio, fin))


def medir(nombre, funcion):
    """Ejecuta una función, mide su duración y devuelve el resultado."""
    inicio = perf_counter()  # Reloj monotónico apropiado para medir intervalos.
    resultado = funcion()
    duracion = perf_counter() - inicio
    print(f"{nombre}: {duracion:.3f} s")
    return resultado


def main():
    # Se usa un máximo moderado de trabajadores para que la comparación sea accesible.
    trabajadores = min(os.cpu_count() or 1, 4)
    tamano_bloque = (CANTIDAD + trabajadores - 1) // trabajadores
    bloques = [
        (inicio, min(inicio + tamano_bloque, CANTIDAD))
        for inicio in range(0, CANTIDAD, tamano_bloque)
    ]
    print(f"CPU disponibles: {os.cpu_count() or 1}")  # 8
    # 4
    print(f"Trabajadores: {trabajadores}")
    # 250_000
    print(f"Tamaño de bloque: {tamano_bloque}")
    # [(0, 250000), (250000, 500000), (500000, 750000), (750000, 1000000)]
    print(f"Bloques de trabajo: {bloques}")

    # La versión secuencial sirve como referencia y calcula exactamente el mismo intervalo.
    resultado_secuencial = medir(
        "Secuencial",
        lambda: sumar_cuadrados(0, CANTIDAD),
    )

    # Los hilos comparten memoria, pero en tareas limitadas por CPU el GIL puede limitar la ejecución paralela.
    def calcular_con_hilos():
        with ThreadPoolExecutor(max_workers=trabajadores) as executor:
            partes = [
                executor.submit(sumar_cuadrados, inicio, fin)
                for inicio, fin in bloques
            ]
            return sum(parte.result() for parte in partes)

    resultado_hilos = medir("Hilos", calcular_con_hilos)

    # Los procesos tienen memoria separada y permiten usar varios núcleos para trabajo de CPU.
    def calcular_con_procesos():
        with ProcessPoolExecutor(max_workers=trabajadores) as executor:
            partes = [
                executor.submit(sumar_cuadrados, inicio, fin)
                for inicio, fin in bloques
            ]
            return sum(parte.result() for parte in partes)

    resultado_procesos = medir("Procesos", calcular_con_procesos)

    # La igualdad verifica que las tres estrategias hicieron el mismo trabajo.
    if not (resultado_secuencial == resultado_hilos == resultado_procesos):
        raise RuntimeError("Los resultados no coinciden; revisa los bloques de trabajo.")

    print(f"Resultado común: {resultado_secuencial}")
    print(f"Trabajadores configurados: {trabajadores}")


if __name__ == "__main__":
    # Los procesos de Windows vuelven a importar el archivo, por eso main va bajo este guard.
    main()
