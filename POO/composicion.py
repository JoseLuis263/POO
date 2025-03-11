class Motor:
    def __init__(self):
        self.temperatura = 0
        self.combustible = 100
        
    def encender(self):
        print("Motor encendido")
        self.temperatura = 100
    
    def apagar(self):
        print("Motor apagado")
        self.temperatura = 0
        
    def acelerar(self):
        if self.combustible > 0:
            self.combustible -= 1
            self.temperatura += 1
            print(f"Acelerando. Temperatura: {self.temperatura}. Combustible: {self.combustible}")
            
        else:
            print("Error: no hay combustible")
            
            
class SistemaElectrico:
    def __init__(self):
        self.bateria = 100
        
    def encender_luces(self):
        if self.bateria > 5:
            self.bateria -= 5
            print(f"Luces encendidas. Batería: {self.bateria}")
        else:
            print("Error: batería baja")
            
    def tocar_claxon(self):
        if self.bateria >= 1:
            print( "Beep Beep")
            self.bateria -= 1
        else:
            print("Error: batería baja")
            
class Coche:
    def __init__(self):
        self.motor = Motor()
        self.sistema_electrico = SistemaElectrico()
        self.velocidad = 0
        
    def arrancar(self):
        self.motor.encender()
        print("Coche arrancado")
        
    def detener(self):
        self.motor.apagar()
        self.velocidad = 0
        print("Coche detenido")
    
    def acelerar(self):
        self.motor.acelerar()
        self.velocidad += 10
        print(f"Velocidad: {self.velocidad} km/h")
        
    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10
            print(f"Frenando. Velocidad: {self.velocidad} km/h")
        else:
            print("Error: el coche ya está detenido")
            
    def encender_luces(self):
        self.sistema_electrico.encender_luces()
        
    def tocar_claxon(self):
        self.sistema_electrico.tocar_claxon()
        
coche = Coche()
coche.arrancar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.encender_luces()
coche.tocar_claxon()
coche.frenar()
coche.frenar()
coche.detener()