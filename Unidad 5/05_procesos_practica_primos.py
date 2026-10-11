"""
Ejemplo 5: práctica aplicada: buscar números primos por bloques en procesos.

Este cálculo usa CPU; los procesos pueden ejecutarlo en distintos núcleos.

Instalación: no se requieren paquetes externos; solo se usa la biblioteca
estándar de Python, así que no hace falta ejecutar pip install.
"""

import os
from concurrent.futures import ProcessPoolExecutor


LIMITE = 100_000  # Se cuentan los primos entre 2 y este límite, incluido.


def es_primo(numero):
    """Indica si un entero es primo probando divisores hasta su raíz cuadrada."""
    if numero < 2:
        return False

    divisor = 2
    # Si divisor * divisor supera al número, no hace falta comprobar más factores.
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def contar_primos(inicio, fin):
    """Cuenta primos en el intervalo semiabierto [inicio, fin)."""
    return sum(1 for numero in range(inicio, fin) if es_primo(numero))


def main():
    # Se limita el ejemplo a cuatro procesos para evitar saturar equipos con muchos núcleos.
    max_procesos = min(os.cpu_count() or 1, 4)
    cantidad_numeros = LIMITE - 1  # El intervalo desde 2 hasta LIMITE contiene LIMITE - 1 valores.
    tamano_bloque = (cantidad_numeros + max_procesos - 1) // max_procesos

    # Cada bloque incluye su inicio y excluye su fin, evitando contar valores dos veces.
    bloques = [
        (inicio, min(inicio + tamano_bloque, LIMITE + 1))
        for inicio in range(2, LIMITE + 1, tamano_bloque)
    ]
    cantidad_trabajadores = min(max_procesos, len(bloques))

    # ProcessPoolExecutor distribuye las llamadas entre procesos reutilizables.
    with ProcessPoolExecutor(max_workers=cantidad_trabajadores) as executor:
        # submit() entrega cada extremo del bloque como parámetro de contar_primos.
        futuros = [
            executor.submit(contar_primos, inicio, fin)
            for inicio, fin in bloques
        ]
        # result() espera el cálculo y propaga cualquier excepción ocurrida en un proceso.
        cantidades = [futuro.result() for futuro in futuros]

    # Se suman las cuentas parciales para obtener el resultado completo.
    print(f"Primos entre 2 y {LIMITE}: {sum(cantidades)}")
    print(f"Bloques procesados: {len(bloques)}")
    print(f"Procesos utilizados: {cantidad_trabajadores}")


if __name__ == "__main__":
    # En Windows, este guard es obligatorio para crear un grupo de procesos correctamente.
    main()
