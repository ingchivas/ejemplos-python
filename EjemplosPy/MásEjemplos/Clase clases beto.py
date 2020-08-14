class Clase:
    var1 = 5
    var2 = 10

    def funcion(self):
        print("Hello world")

objeto1 = Clase()
objeto2 = Clase()

Clase.var1 = 25

print(objeto1.var1)
print(objeto2.var2)

objeto1.funcion()
print(objeto1.var1)



class complejos:
    def numeros(self,r,i):
        self.r = r
        self.i = i
    
    def calculadora(self,c):
        self.c = c
    
    def suma():
        cantidad = self.r + self.c
        self.c += cantidad
        print(cantidad, i)
    
    def vuelta():
        print(self.c)

objeto3 = complejos()
