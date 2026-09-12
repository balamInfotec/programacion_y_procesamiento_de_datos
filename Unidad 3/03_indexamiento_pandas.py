"""
Indexamiento en pandas
"""

import pandas as pd

ventas = pd.DataFrame(
    {
        "producto": ["Cuaderno", "Pluma", "Mochila", "Termo", "Lapiz"],
        "sucursal": ["Centro", "Norte", "Centro", "Sur", "Norte"],
        "unidades": [10, 35, 4, 8, 50],
        "precio": [45.50, 12.00, 380.00, 250.00, 8.50],
    },
    index=["V001", "V002", "V003", "V004", "V005"],
)

print(f"\nVentas:\n{ventas}")

# Acceder a columnas
print("\nUna columna:")
print(ventas["producto"])

# Acceso a varias columnas
print("\nVarias columnas:")
print(ventas[["producto", "precio"]])

# Podemos utilizar iloc para obtener un conjunto de información (rango)
print("\nPrimeras dos filas con iloc:")
print(ventas.iloc[0:2])

# Obtenemos una celda, un único valor
print(f"\nFila 3, columna 1 con iloc: {ventas.iloc[2, 1]}")

# Obtener un rango de información del dataFrame
print(f"\nFilas 1 a 3 y columnas 0 a 2 con iloc: \n{ventas.iloc[0:3, 0:2]}")

# Con loc podemos obtener información utilizando las etiquetas definidas en las columnas
# y en los índices
print(f"\nFila V003, columna precio con loc: {ventas.loc['V003', 'precio']}")
print(ventas.loc["V003"])

ventas["importe"] = ventas["unidades"] * ventas["precio"]
print(f"\nVentas con importe:\n{ventas}")

print(f"\nVentas mayores a 500:\n")
print(ventas.loc[ventas["importe"] > 500, ["producto", "importe"]])

ventas.loc[ventas["sucursal"] == "Norte", "region"] = "Norte"
ventas.loc[ventas["sucursal"] != "Norte", "region"] = "Otra"

# Vamos a imprimir el dataFrame con la columna región
print(f"\nVentas: {ventas}")

# Obtenemos una celda mediante el uso de etiquetas
print(f"\nCelda mediante at:\n{ventas.at["V003", "region"]}")

# Obtenemos una celda mediante el uso de posiciones
print(f"\nCelda mediante iat:\n{ventas.iat[2, 4]}")


