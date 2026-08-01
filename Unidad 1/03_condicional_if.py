condicion = True
if condicion:
    print("Entró al bloque verdadero")
    
condicion = False

if condicion:
    print("Entró al bloque verdadero")
else:
    print("Entró al bloque falso")
    
condicion = 50
temperatura = 55

print(condicion < 0)
print(temperatura >= 50)
print(condicion < 0 or temperatura >= 50)

# Evaluación de dos expresiones mediante un operador or
if condicion < 0 or temperatura >= 50:
    print("Entró al bloque verdadero")
elif condicion <20:
    print("Entró al siguiente bloque condicional")
else:
    print("Entró al bloque falso")
    
numero_uno = 10
numero_dos = -1
print("Inicia último bloque")
# Evaluación de dos expresiones condicionales mediante un operador and
if numero_uno < 0 and numero_dos < 0:
    print("Ingresó al bloque verdadero")
    
opcion = 0
# Nos permite evaluar una variable
match opcion:
    case 1:
        # Si la variable toma el valor 1, ejecutaría este código
        print("Es uno")
    case 2:
        print("Es dos")
    case _:
        print("Ninguno se cumple")