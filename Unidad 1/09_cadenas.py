texto = "Hola" # Definimos una cadena de texto
texto = 'Hola mundo' # También la podemos definir con comillas simples

print(f"Caracter: {texto[0]}") # Podemos acceder a caracteres específicos

# texto[0] = "h" # CUIDADO, python no permite actualizar cadenas de texto, esto da error

texto_nuevo = texto[0] + " complemento" # En todo caso, deberíamos crear una cadena nueva
print(f"Texto nuevo: {texto_nuevo}")

longitud_cadena = len(texto_nuevo) # Así podemos obtener la longitud de una cadea
concatenacion = "Hola " + " Mundo" # Así podemos concatenar cadenas (unir)
invertir = concatenacion[::-1] # De esta forma invertimos la cadena
nuevo_token = concatenacion[0:3] # Podemos obtener una parte de la cadena, desde el índice 0 hasta el 3

# Funciones útiles
print(f"Mayúsculas: {nuevo_token.upper()}") # Cambiamos todo a mayúsculas (ojo: no modifica la cadena original)
print(f"Minúsculas: {nuevo_token.lower()}") # Todo a minúsculas

indice = concatenacion.find("Mun")
print(f"La palabra 'Mun' aparece en la posición: {indice}")
print(f"La palabra inicia con Mun? {concatenacion.startswith("Mun")}, o finaliza con 'do'?: {concatenacion.endswith("do")}")

cadena_reemplazo = concatenacion.replace("o", "r") # Reemplazamos todas las letras o's por r's
print(f"Cadena reemplazada: {cadena_reemplazo}")

cadena = "Hola {}, tienes {} años."
print(cadena.format("Luis", 38)) # Permite formatear de otra manera las cadenas

#cadena = "C:\Users\Luis\Documentos" # Esto marca error! Utilizar raw strings
cadena = r"C:\Users\Luis\Documentos" # Anteponiendo r, utilizamos raw strings en cadenas, esto ya está bien
print(f"Ruta: {cadena}")

texto = """
Texto
mutilínea
si es
necesario
"""

print(f"Texto multilínea: {texto}")

resultado = texto.isalpha() # Evaluamos si la cadena contiene solo letras
print(f"Resultado de la evaluación: {resultado}")
resultado = texto.isdigit() # Si contiene solo números
resultado = texto.isalnum() # Letras y números
resultado = texto.isspace() # Solo espacios