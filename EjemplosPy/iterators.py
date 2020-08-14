class Numeros:
    def __iter__(self):
        self.a = 1
        return self
    

    def __next__(self):
        while self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

clase = Numeros()
iterador = iter(clase)

print(x)
for i in iterador:
    print(i)