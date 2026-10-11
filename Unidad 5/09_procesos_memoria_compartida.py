"""
Ejemplo 9: compartir un valor numérico mediante multiprocessing.Value.

Cada proceso incrementa el mismo contador. A diferencia de Queue, Value
representa un dato compartido en memoria, no una secuencia de mensajes.

Instalación: no se requieren paquetes externos; solo se usa la biblioteca
estándar de Python, así que no hace falta ejecutar pip install.
"""

import multiprocessing


def incrementar(contador, repeticiones):
    """Incrementa el valor compartido de forma segura."""
    for _ in range(repeticiones):
        # Adquiere el cerrojo asociado al Value (contador) para que el incremento completo no se intercale con otro proceso.
        with contador.get_lock():
            contador.value += 1


if __name__ == "__main__":
    # El guard es necesario en Windows para que los procesos hijos no vuelvan a crear trabajadores.
    cantidad_procesos = 3
    repeticiones_por_proceso = 5

    # Value crea un entero en memoria compartida: cada proceso recibe acceso al mismo valor,
    # no una copia local independiente como ocurriría con un int normal.
    # 'i' indica el tipo entero con signo de ctypes; 0 es el valor inicial del contador.
    # lock=True asocia un cerrojo para proteger el acceso al valor compartido.
    contador = multiprocessing.Value("i", 0, lock=True)

    procesos = [
        multiprocessing.Process(
            target=incrementar,  # Cada proceso ejecuta la misma función sobre el valor compartido.
            args=(contador, repeticiones_por_proceso),  # Se pasa el objeto compartido, no una copia del entero.
            name=f"contador-{numero}",
        )
        for numero in range(cantidad_procesos)
    ]

    # Todos los procesos se inician antes de esperarlos para que puedan trabajar simultáneamente.
    for proceso in procesos:
        proceso.start()

    # join() espera a que cada trabajador termine antes de leer el resultado.
    for proceso in procesos:
        proceso.join()

    esperado = cantidad_procesos * repeticiones_por_proceso
    print(f"Contador compartido: {contador.value}")
    print(f"Resultado esperado: {esperado}")