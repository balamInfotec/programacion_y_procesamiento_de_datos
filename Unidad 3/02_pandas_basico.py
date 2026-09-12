"""
Pandas básico - operaciones básicas
"""

import pandas as pd
# Definimos la serie con índice
precios = pd.Series([100, 200, 300, 400], index=['A', 'B', 'C', 'D'])
print(f"\nPrecios con índice:\n{precios}")
# Definimos la serie sin índice
precios = pd.Series([100, 200, 300, 400])
print(f"\nPrecios sin índice:\n {precios}")

datos = {
    "producto": ["Cuaderno", "Pluma", "Mochila", "Termo", "Lapiz"],
    "categoria": ["Papeleria","Papeleria","Accesorios","Accesorios","Papeleria"],
    "precio": [45.50, 12.00, 380.00, 250.00, 8.50],
    "existencias": [20, 80, 12, 15, 100],
}

print(f"Datos de ejemplo: {datos}")

# Convertimos el diccionario de datos en un objeto DataFrame, para que pandas pueda operar sobre él
inventario = pd.DataFrame(datos)
print(f"\nInventario:\n{inventario}")

# Leer datos desde un archivo CSV
inventario = pd.read_csv("02_pandas_basico.csv")
print(f"\nDatos del inventario obtenidos desde CSV:\n{inventario}")

# Imprimir las primeras 3 filas
print(f"\nPrimeras 3 filas del inventario:\n{inventario.head(3)}")

# Imprimir las últimas 3 filas
print(f"\nÚltimas 3 filas del inventario:\n{inventario.tail(3)}")

# Imprimir información del DataFrame
print(f"\nInformación del DataFrame:")
inventario.info()

# Generar estadísticas 'generales' usando describe
print(f"\nEstadísticas generales del DataFrame:")
print(inventario.describe())

# Podemos obtener los nombres de las columnas
print(f"\nNombres de las columnas del DataFrame:\n{inventario.columns}")

# Podemos obtener con shape la cantidad de filas y columnas
print(f"\nCantidad de filas y columnas del DataFrame:\n{inventario.shape}")

# Imprimir los tipos de datos de nuestro dataFrame
print(f"\nTipos de datos: {inventario.dtypes}")

# Podemos obtener una serie del dataFrame, o sea una columna
precios = inventario["precio"]
print(f"\nPrecios:\n{precios}")

# Podemos hacer cálculos sobre las columnas o variables de nuestro dataFrame

inventario["valor_inventario"] = (inventario["precio"] * inventario["existencias"])
print(f"\nInventario con valor de inventario:\n{inventario}")

# Podemos almacenar datos en un archivo CSV
inventario.to_csv("02_pandas_basico_salida.csv", index=False)
print("Los datos se almacenaron!!!")



