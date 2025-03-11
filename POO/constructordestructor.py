class Miclase:
    def __init__(self, nombre):
        self.nombre = nombre
        print("Se ha creado el objeto", self.nombre)
        
    def __del__(self):
        print("Se ha destruido el objeto", self.nombre)
        
objeto1 = Miclase("objeto1")
objeto2 = Miclase("objeto2")
objeto3 = Miclase("objeto3")
