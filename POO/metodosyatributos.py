class Miclase:
    contador = 0
    
    def __init__(self):
        Miclase.contador += 1
        
    @classmethod
    def get_contador(cls):
        return cls.contador
    
obj1 = Miclase()
print("Contador de objetos:", Miclase.get_contador())
obj2 = Miclase()
print("Contador de objetos:", Miclase.get_contador())