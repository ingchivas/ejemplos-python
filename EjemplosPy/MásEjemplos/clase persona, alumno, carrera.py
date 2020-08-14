class Persona:
    def __init__(self, nombre, apellido):
        self.n = nombre
        self.a = apellido
    
    def printpersona(self):
        print(self.n, self.a)

class Student(Persona):
    def __init__ (self, nombre, apellido, universidad, aingreso):
        super(). __init__(nombre, apellido)
        self.univ = universidad
        self.aing = aingreso
    
    def printstudent(self):
        Persona.printpersona(self)
        print(self.univ, self.aing)

class Carrera(Student):
    def __init__ (self,nombre, apellido, universidad, aingreso, carrera, graduacion):
        super().__init__(nombre, apellido, universidad, aingreso)
        self.c = carrera
        self.g = graduacion
    
    def welcome(self):
        print("Bienvenido:", self.n, self.a, "a la", self.univ, self.aing)
        print(self.c, self.g)

Grape = Persona("Juan", "Cruz")
Grape.printpersona()

Andy = Student("Andrea", "Chavez", "Anahuac", 2020)
Andy.printpersona()
Andy.printstudent()

Beto = Carrera("Beto", "Lopez", "UP", 2020, "Sistemas",2025)
Beto.welcome()

Kat = Carrera("Katerina", "Soto", "TEC", 2020, "Mecanica", 2025)
Kat.printpersona()
Kat.printstudent()
Kat.welcome()