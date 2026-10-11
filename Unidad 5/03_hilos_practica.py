"""
Ejemplo 3: práctica aplicada: analizar varios archivos de registro con hilos.

La práctica crea registros de demostración en una carpeta temporal y cuenta
sus niveles de error en paralelo, como se haría al revisar varios logs.

Instalación: no se requieren paquetes externos; solo se usa la biblioteca
estándar de Python, así que no hace falta ejecutar pip install.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from tempfile import TemporaryDirectory


def contar_errores(ruta):
    """Devuelve el nombre del archivo y cuántas líneas contienen ERROR."""
    errores = 0

    # utf-8 es explícito para leer archivos con texto de forma consistente.
    with ruta.open(encoding="utf-8") as archivo:
        for linea in archivo:
            if "ERROR" in linea:
                errores += 1

    return ruta.name, errores


def crear_logs_de_ejemplo(carpeta):
    """Genera entradas ficticias para que la práctica se pueda ejecutar sola."""
    registros = {
        "api.log": [
            "INFO servicio iniciado\n",
            "ERROR no se pudo conectar a la base de datos\n",
            "INFO reintento realizado\n",
        ],
        "web.log": [
            "INFO solicitud recibida\n",
            "ERROR respuesta 500\n",
            "ERROR tiempo de espera agotado\n",
        ],
        "worker.log": [
            "INFO tarea procesada\n",
            "INFO cola vacía\n",
        ],
    }

    for nombre, lineas in registros.items():
        ruta = carpeta / nombre
        # newline="" evita que Python transforme los saltos de línea al escribir.
        with ruta.open("w", encoding="utf-8", newline="") as archivo:
            archivo.writelines(lineas)


def main():
    # La carpeta temporal se elimina automáticamente al salir del bloque.
    with TemporaryDirectory() as carpeta_temporal:
        carpeta = Path(carpeta_temporal)
        crear_logs_de_ejemplo(carpeta)

        # Se descubre la lista de archivos antes de iniciar los trabajadores.
        archivos = sorted(carpeta.glob("*.log"))
        cantidad_trabajadores = min(4, len(archivos))  # No se crean más hilos que tareas.
        print(f"Cantidad de trabajadores: {cantidad_trabajadores}")
        resultados = []

        # ThreadPoolExecutor administra la creación y reutilización de hilos.
        with ThreadPoolExecutor(max_workers=cantidad_trabajadores) as executor:
            # submit() programa cada archivo y devuelve un Future para consultar el resultado.
            futuros = [
                executor.submit(contar_errores, ruta)
                for ruta in archivos
            ]

            # as_completed() permite mostrar cada resultado conforme esté listo.
            for futuro in as_completed(futuros):
                resultados.append(futuro.result())  # Propaga explícitamente errores de la tarea.

        # Se ordenan los resultados para que la salida sea fácil de comparar entre ejecuciones.
        for nombre, errores in sorted(resultados):
            print(f"{nombre}: {errores} error(es)")

        print(f"Total: {sum(errores for _, errores in resultados)} error(es)")


if __name__ == "__main__":
    # El punto de entrada explícito también evita iniciar la práctica al importar este archivo.
    main()
