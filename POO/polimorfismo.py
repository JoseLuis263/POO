class Ave:
    def volar(self):
        pass
    
class Aguila(Ave):
    def volar(self):
        return "El águila vuela muy alto"
    
class Pinguino(Ave):
    def volar(self):
        return "El pingüino no puede volar"

aguila = Aguila()
pinguino = Pinguino()

aves = [aguila, pinguino]

def hacer_volar(ave):
    print(ave.volar())
    
for i in range(len(aves)):
    hacer_volar(aves[i])