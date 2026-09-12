"""
    Series de tiempo
"""

import pandas as pd

datos = pd.DataFrame(
    {
        "fecha": [
            "2025-01-05",
            "2025-01-18",
            "2025-02-03",
            "2025-02-21",
            "2025-03-10",
            "2025-03-28",
            "2025-04-15",
            "2025-04-29",
        ],
        "ventas": [1200, 1450, 1320, 1680, 1550, 1900, 2100, 2300],
        "visitas": [80, 95, 88, 110, 105, 125, 140, 150],
    }
)

print(f"Tipos de datos del dataFrame:\n{datos.dtypes}")

# Antes de trabajar con datos de fechas o tiempos, debemos convertirlos
datos["fecha"] = pd.to_datetime(datos["fecha"])

# imprimir nuevamente los tipos de datos
print(f"Tipos de datos del dataFrame:\n{datos.dtypes}")

# set_index establece la columna fecha como índice
datos = datos.set_index("fecha").sort_index()

print(f"Conjunto de datos con fecha como índice:\n {datos}")

# Quiero obtener los datos correspondientes al mes de febrero:
print(f"Datos del mes de febrero:{datos.loc["2025-02"]}")

# Podemos obtener el mes
datos["mes"] = datos.index.month
datos["dia_semana"] = datos.index.day_name()

print(f"\nDatos:\n{datos}")

# Obtener las ventas mensuales de mi conjunto de datos
ventas_mensuales = datos["ventas"].resample("MS").sum()
visitas_mensuales = datos["visitas"].resample("ME").sum()

print(f"\nVentas mensuales:\n{ventas_mensuales}")
print(f"\nVisitas mensuales:\n{visitas_mensuales}")

# rolling calcula una ventana móvil
# Vamos a obtener el promedio de dos observaciones
datos["promedio_movil"] = datos["ventas"].rolling(2).mean()
print(f"Promedio módil de ventas: {datos[["ventas", "promedio_movil"]]}")


