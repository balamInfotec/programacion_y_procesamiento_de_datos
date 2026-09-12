"""
    Datos tabulares
"""
columnas = ["productos", "categorias", "precio", "existencias"]
print(f"Columnas: {columnas}")

productos = [
    ["Cuaderno", "Papeleria", 45.50, 20],
    ["Pluma", "Papeleria", 12.00, 80],
    ["Mochila", "Accesorios", 380.00, 12],
    ["Termo", "Accesorios", 250.00, 15],
]

print("\nTabla representada como lista de listas:")
print(columnas)
for producto in productos:
    print(producto)


productos_con_nombre = [
    {
        "producto": "Cuaderno",
        "categoria": "Papeleria",
        "precio": 45.50,
        "existencias": 20,
    },
    {
        "producto": "Pluma",
        "categoria": "Papeleria",
        "precio": 12.00,
        "existencias": 80,
    },
]

print("\nTabla representada como lista de diccionarios:")
for producto in productos_con_nombre:
    print(producto)
    
total_productos = sum(producto["existencias"] for producto in productos_con_nombre)
print(f"\nTotal de productos en existencia: {total_productos}")

valor_inventario = sum(producto["precio"] * producto["existencias"] for producto in productos_con_nombre)
print(f"Valor total del inventario: {valor_inventario}")