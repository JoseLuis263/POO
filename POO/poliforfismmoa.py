import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other): # Método especial para sumar objetos
        return Punto(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Punto(self.x - other.x, self.y - other.y)
    
    def __str__(self): # Método especial para representar un objeto como string
        return f"Punto({self.x}, {self.y})"
    
    def distancia_al_origen(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    @staticmethod
    def punto_medio(p1, p2):
        x = (p1.x + p2.x) / 2
        y = (p1.y + p2.y) / 2
        return Punto(x, y)
        
    
punto1 = Punto(1, 3)
punto2 = Punto(2, 5)

p3 = punto1 + punto2
print(p3)

p3 = punto2 - punto1
print(p3)

print(punto1.distancia_al_origen())
print(punto2.distancia_al_origen())

pm = Punto.punto_medio(punto1, punto2)
print(pm)

# def sumar_puntos(p1, p2):
#     x = p1.x + p2.x
#     y = p1.y + p2.y
#     p3 = Punto(x, y)
#     return p3

# punto3 = sumar_puntos(punto1, punto2)
# print(punto3.x, punto3.y)