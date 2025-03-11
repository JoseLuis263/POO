# Programacion Orinetada a Objetos

#Encapsulamiento
#Agrupar datos y metodos que operan sobre una unica unidad llamada clase


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre # __nombre es un atributo privado
        self.__edad = edad
        
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("Edad incorrecta")
    
persona = Persona("juan", 30)
print(persona.get_nombre()) 

persona.set_nombre("Pedro")
print(persona.get_nombre())

print( persona.get_edad() )
persona.set_edad(10)
print( persona.get_edad() )