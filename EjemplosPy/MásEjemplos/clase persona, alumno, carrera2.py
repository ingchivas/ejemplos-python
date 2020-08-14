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
        print(self.n, self.a, self.univ, self.aing)

class Carrera(Student):
    def __init__ (self, nombre, apellido, universidad, aingreso, carrera, graduacion):
        super(). __init__(nombre,apellido,universidad,aingreso)
        self.c = carrera
        self.g = graduacion
    
    def welcome(self):
        print("Bienvenido:", self.n, self.a, "a la", self.univ, self.aing)
        print(self.c, self.g)

Beto = Persona("BETO", "LOPEZ")
Beto.printpersona()

Luis = Student("Luis", "Cf", "UP", 2020)
Luis.printpersona()
Luis.printstudent()

Kat = Student("Kat", "Soto", "TEC", 2020)
Kat = Carrera("Kat", "Soto", "TEC", 2020, "Mecanica", 2025)
Kat.welcome()