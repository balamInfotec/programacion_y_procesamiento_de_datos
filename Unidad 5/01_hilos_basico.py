"""
Ejemplo 1: crear y coordinar hilos.

Instalación: no se requieren paquetes externos; solo se usa la biblioteca
estándar de Python, así que no hace falta ejecutar pip install.
"""

import threading
import time
from time import perf_counter

def tarea(nombre, segundos):
    """Simula una tarea que espera y después informa que terminó."""
    print(f"{nombre}: inicio")
    time.sleep(segundos)  # Simula una espera de entrada/salida, como una respuesta de red.
    print(f"{nombre}: fin después de {segundos} segundo(s)")

def ejecucion_secuencial():
    """Ejecuta las tareas de manera secuencial, una tras otra."""
    tarea("Tarea A", 2)
    tarea("Tarea B", 1)
    print("Todas las tareas terminaron.")

def ejecucion_hilos():
    """Ejecuta las tareas en hilos separados, permitiendo que se solapen."""
    # El nombre ayuda a identificar cada hilo al leer la salida.
    hilo_1 = threading.Thread(
        target=tarea,  # Se pasa la función; no se llama aquí con tarea(...).
        args=("Tarea A", 2),  # args contiene, en orden, los argumentos de tarea.
        name="hilo-a",
    )
    hilo_2 = threading.Thread(
        target=tarea,
        args=("Tarea B", 1),
        name="hilo-b",
    )

    # start() inicia cada hilo; llamar tarea() directamente sería secuencial.
    hilo_1.start()
    hilo_2.start()

    # join() espera a que cada hilo termine antes de continuar con el programa.
    hilo_1.join()
    hilo_2.join()

    print("Todas las tareas terminaron.")


if __name__ == "__main__":
    print("Ejecución secuencial:")
    inicio = perf_counter()
    ejecucion_secuencial()
    duracion = perf_counter() - inicio
    print(f"Duración de la ejecución secuencial: {duracion:.3f} s")
    
    print("\nEjecución con hilos:")
    inicio = perf_counter()
    ejecucion_hilos()
    duracion = perf_counter() - inicio
    print(f"Duración de la ejecución con hilos: {duracion:.3f} s")

    
