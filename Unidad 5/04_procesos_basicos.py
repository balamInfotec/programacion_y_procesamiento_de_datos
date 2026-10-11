"""
Ejemplo 4: crear procesos independientes.

Instalación: no se requieren paquetes externos; solo se usa la biblioteca
estándar de Python, así que no hace falta ejecutar pip install.
"""

import multiprocessing
import os
import time


def tarea(nombre, segundos):
    """Muestra qué proceso ejecuta una tarea y simula un trabajo breve."""
    print(f"{nombre}: PID {os.getpid()} inicia")
    time.sleep(segundos)  # La espera ilustra que ambos procesos pueden progresar a la vez.
    print(f"{nombre}: PID {os.getpid()} termina")


if __name__ == "__main__":
    # En Windows los procesos nuevos importan el módulo; este guard impide que se creen en cada importación.
    proceso_1 = multiprocessing.Process(
        target=tarea,  # La función debe estar definida a nivel de módulo para que pueda iniciarse en Windows.
        args=("Proceso A", 2),  # Los argumentos se envían al proceso hijo como una tupla.
        name="proceso-a",
    )
    proceso_2 = multiprocessing.Process(
        target=tarea,
        args=("Proceso B", 1),
        name="proceso-b",
    )

    # start() crea los procesos; no se ejecuta la función en el proceso principal.
    proceso_1.start()
    proceso_2.start()

    # join() mantiene vivo al proceso principal hasta que terminen los hijos.
    proceso_1.join()
    proceso_2.join()

    # exitcode permite comprobar si cada proceso finalizó normalmente (código 0).
    print(f"Código de salida A: {proceso_1.exitcode}")
    print(f"Código de salida B: {proceso_2.exitcode}")
