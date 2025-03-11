class A:
    def metodo(self):
        print("Soy el método de la clase A")
        
class B:
    def metodo(self):
        print("Soy el método de la clase B")
        
class C(B, A):
    def metodo(self):
        print("Soy el método de la clase C")

obj = C()
print(obj.metodo())