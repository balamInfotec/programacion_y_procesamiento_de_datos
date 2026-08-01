class Calculadora:
    def __init__(self, numero_uno, numero_dos): # Podemos solicitar los parámetros al realizar la instancia de la clase
        self._numero_uno = numero_uno # Definimos los atributos necesarios para la clase
        self._numero_dos = numero_dos
        
    def calcular(self): # Definimos el método de la clase (comportamiento)
        return self._numero_uno + self._numero_dos
    
obj = Calculadora(12, 2) # Al instanciar la clase, pasamos los parámetros necesarios, sino, python generará un error
resultado = obj.calcular() # Llamamos al método de la clase a través de la variable obj
print(f"Resultado: {resultado}") # Imprimimos el resultado con f-strings