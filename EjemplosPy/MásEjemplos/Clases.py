class superhero:
    def __init__(self, nombre, poder, ubicacion):
        self.n = nombre
        self.p = poder
        self.u = ubicacion
    
    def printheroe(self):
        print(self.n , self.p, self.u)

superheroe1 = superhero("Spiderman", "araña" , "Queens")
superheroe2 = superhero("Steve", "supersoldado", "Brooklyn")

print(superheroe1.n, superheroe1.p , superheroe1.u)
superheroe2.printheroe()

class asistencia:
    def ayudante(self, ayudantex):
        self.a = ayudantex
    
    def printayudante():
        print(self.a)

ayudante1 = asistencia()
ayudante1 = ayudante1.ayudante("Morales")
print(ayudante1)

