class Animal:# Definimos la clase padre
    def hablar(self):# Definimos un comportamiento genérico aplicable a todos los animales (método)
        print("Sonido genérico!!!")
        
class Perro(Animal): # Definimos una nueva clase (hija), que hereda de la clase Animal
    def hablar(self): # Sobreescribimos el método hablar (polimorfismo)
        print("Ladrar!!!")
        
class Gato(Animal): # Definimos otra clase (hija), que hereda de la clase Animal
    def hablar(self): # Sobreescribimos también el método hablar (polimorfismo)
        print("Maullar!!!!")
        
obj_perro = Perro() # Instanciamos la clase Perro para poder utilizar los métodos y propiedades de la misma
obj_gato = Gato() # Instanciamos la clase Gato
obj_perro.hablar() # Ejecutamos el método hablar sobreescrito por la clase Perro
obj_gato.hablar() # Ejecutamos el método hablar sobreescrito por la clase Gato