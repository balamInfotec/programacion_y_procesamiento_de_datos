# Utilizamos la función range para generar un rango que pueda ser
# iterado por for
for i in range(5): # Al especificar solamente un número, el rango va desde 0 hasta 5 (sin considerar el 5)
    print(i)
    
print("Otro")

for i in range(2, 10, 2): # Si especificamos otros 2 parámetros, podemos especificar: inicio, fin, incremento
    if i == 4:
        break # La sentencia break permite finalizar de manera anticipada la estructura repetitiva
    print(i)
    
print("Otro")

for i in range(2, 10, 2):
    if i == 4:
        continue # La sentencia continue permite ignorar el código que está debajo para ir a la siguiente iteración
    print(i)
    
opcion = 0

while opcion != 3: # Cuidado! con break, si la condición nunca llega a ser falsa, podríamos generar un ciclo infinito de ejecuciones
    if opcion == 0:
        break
    print("Ciclo while")
    opcion = 3
else:
    print("Finalizó ciclo while") # Este código se ejecuta al final de la ejecución de while, siempre y cuando no haya finalizado por break