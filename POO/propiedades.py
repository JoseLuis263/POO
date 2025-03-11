class Miclase:
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, nuevo_valor):
        if nuevo_valor > 0:
            self._valor = nuevo_valor
        else:
            print("Error: el valor debe ser mayor que 0")
            
            
obj = Miclase(10)
print(obj.valor)
obj.valor = 15
print(obj.valor)
obj.valor = -5