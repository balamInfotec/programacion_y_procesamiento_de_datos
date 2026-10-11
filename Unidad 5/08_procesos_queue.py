"""
Ejemplo 8: enviar datos entre procesos mediante Queue.

El proceso principal manda números al trabajador y recibe los resultados.

Instalación: no se requieren paquetes externos; solo se usa la biblioteca
estándar de Python, así que no hace falta ejecutar pip install.
"""

import multiprocessing


def trabajador(cola_entrada, cola_salida):
    """Recibe números, calcula sus cuadrados y devuelve cada resultado."""
    while True:
        dato = cola_entrada.get()  # Espera hasta que haya un mensaje disponible.

        if dato is None:  # None es un mensaje especial para indicar que no hay más trabajo.
            break

        numero, cuadrado = dato, dato * dato
        cola_salida.put((numero, cuadrado))  # Envía el resultado al proceso principal.


if __name__ == "__main__":
    # El guard es necesario en Windows para que los procesos hijos no vuelvan a crear trabajadores.
    cola_entrada = multiprocessing.Queue()  # Canal por el que el proceso principal envía tareas.
    cola_salida = multiprocessing.Queue()  # Canal distinto para que el trabajador devuelva resultados.

    proceso = multiprocessing.Process(
        target=trabajador,  # Función que ejecutará el proceso trabajador.
        args=(cola_entrada, cola_salida),  # Se pasan las colas para que ambos procesos las compartan.
        name="trabajador-cuadrados",
    )
    proceso.start()  # Inicia el trabajador antes de enviar los datos.

    numeros = [3, 5, 8]  # Pequeño conjunto de datos de ejemplo.
    for numero in numeros:
        cola_entrada.put(numero)  # put() envía un elemento por la cola de entrada.

    cola_entrada.put(None)  # El mensaje centinela indica al trabajador que ya terminó la entrada.

    resultados = []
    for _ in numeros:
        resultados.append(cola_salida.get())  # get() espera cada resultado que el trabajador envía.

    proceso.join()  # Espera el cierre del trabajador después de recoger todas las respuestas.

    for numero, cuadrado in sorted(resultados):
        print(f"{numero} al cuadrado = {cuadrado}")

    # close() indica que el proceso principal ya no usará estas colas.
    cola_entrada.close()
    cola_salida.close()
