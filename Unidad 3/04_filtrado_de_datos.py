"""
Filtrado de datos en pandas

"""

import pandas as pd


ventas = pd.DataFrame(
    {
        "producto": [
            "Cuaderno",
            "Pluma",
            "Mochila",
            "Termo",
            "Lapiz",
            "Cuaderno",
        ],
        "categoria": [
            "Papeleria",
            "Papeleria",
            "Accesorios",
            "Accesorios",
            "Papeleria",
            "Papeleria",
        ],
        "sucursal": ["Centro", "Norte", "Centro", "Sur", "Norte", "Sur"],
        "unidades": [2, 4, 4, 8, 50, 12],
        "precio": [45.50, 12.00, 380.00, 250.00, 8.50, 45.50],
    }
)

ventas["importe"] = ventas["unidades"] * ventas["precio"]
print(f"Ventas:\n{ventas}")

# Filtrar con condición booleana
ventas_grandes = ventas[ventas["importe"] >= 400]
print(f"\nVentas grandes:\n{ventas_grandes}")

# Filtrar por más de una condición
papeleria_norte = ventas[
    (ventas["categoria"] == "Papeleria")
    & (ventas["sucursal"] == "Norte")
]

print(f"\nFiltrando por papelería en la sucursal Norte:\n{papeleria_norte}")

papeleria_o_sur = ventas[
    (ventas["categoria"] == "Papeleria")
    | (ventas["sucursal"] == "Sur")
]
print("\nVentas de papeleria o de la sucursal Sur:")
print(papeleria_o_sur)

productos_seleccionados = ventas[
    ventas["producto"].isin(["Cuaderno", "Termo"])
]
print("\nVentas de Cuadernos y Termos:")
print(productos_seleccionados)

# Podemos utilizar sort_values para ordenar mediante una columna
por_importe = ventas.sort_values("importe", ascending=True)
print("\nVentas ordenadas de mayor a menor importe:")
print(por_importe[["producto", "sucursal", "importe"]])

# Podemos agrupar utilizando groupby
resumen_categoria = ventas.groupby("categoria", as_index=False).agg(
    # Creamos nuevas columnas con nombres personalizados y agregamos funciones de agregación.
    # El primer parámetro es el nombre de la nueva columna, 
    # el segundo es una tupla con el nombre de la columna original y la función de agregación.
    ventas_totales=("importe", "sum"),
    unidades_totales=("unidades", "sum"),
    precio_promedio=("precio", "mean"),
)

print("\nResumen por categoria:")
print(resumen_categoria)

# Resumen por sucursal
resumen_sucursal = ventas.groupby("sucursal", as_index=True).agg(
    importe_total=("importe", "sum"),
    productos_totales=("producto", "count"),
)
print("\nResumen por sucursal:")
print(resumen_sucursal)