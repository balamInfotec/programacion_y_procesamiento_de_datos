"""
Ejemplo 2: compartir datos entre hilos de forma segura.

Instalación: no se requieren paquetes externos; solo se usa la biblioteca
estándar de Python, así que no hace falta ejecutar pip install.
"""

import threading
import time

contador = 0
cerrojo = threading.Lock()  # El Lock evita que dos hilos actualicen a la vez el contador.


def incrementar(cantidad, retraso):
    global contador  # Indica que se actualizará la variable definida fuera de la función.

    for _ in range(cantidad):
        # El bloque with adquiere el cerrojo y lo libera incluso si ocurre un error.
        with cerrojo:
            valor_leido = contador  # Se lee el valor actual del contador.
            time.sleep(retraso)  # Simula una espera de entrada/salida, como una respuesta de red.
            contador = valor_leido + 1  # Se incrementa el valor leído y se escribe de nuevo en la variable compartida.


if __name__ == "__main__":
    retrasos = [0.0001, 0.0002, 0.0003, 0.0004]
    repeticiones = 10_000  # Cada hilo hará esta cantidad de incrementos.
    cantidad_hilos = 4  # Se crean varios trabajadores para compartir el mismo contador.

    # Se conserva cada objeto Thread para poder iniciarlo y esperarlo más adelante.
    hilos = [
        threading.Thread(
            target=incrementar,  # La función ejecutada por cada hilo.
            args=(repeticiones, retrasos[numero], ),  # La coma crea una tupla de un solo argumento.
            name=f"contador-{numero}",
        )
        for numero in range(cantidad_hilos)
    ]

    # Se inician todos antes de esperar para que el trabajo pueda solaparse.
    for hilo in hilos:
        hilo.start()

    # Se espera a todos antes de leer el resultado final.
    for hilo in hilos:
        hilo.join()

    # El resultado esperado permite comprobar que las actualizaciones no se perdieron.
    print(f"Resultado: {contador}")
    print(f"Esperado: {repeticiones * cantidad_hilos}")
