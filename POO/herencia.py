class Animal():
    def __init__(self, nombre):
        self.nombre = nombre
        
    def sonido(self):
        pass
    
class Perro(Animal):
    def sonido(self):
        return "Guau"
    
class Gato(Animal):
    def sonido(self):
        return "Miau"
    
perro = Perro("Firulais")
gato = Gato("Garfield")

print(perro.nombre)
print(perro.sonido())
print(gato.nombre)
print(gato.sonido())    