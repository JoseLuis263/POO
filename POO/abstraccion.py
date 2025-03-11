from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return 3.14 * self.radio * self.radio
    
    def perimetro(self):
        return 2 * 3.14 * self.radio
    
circulo = Circulo(5)
print("Área del círculo:", circulo.area())
print("Perímetro del círculo:", circulo.perimetro())

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.base * 3
    
triangulo = Triangulo(5, 3)
print("Área del triángulo:", triangulo.area())
print("Perímetro del triángulo:", triangulo.perimetro())
