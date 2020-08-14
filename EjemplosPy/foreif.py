promedio = 0
materias = int(input('dime tu num de materias'))
for i in range(materias):
    sumamat = float(input('materia:'))
    promedio = float(sumamat) + float(promedio)

final = float(promedio)/materias
print(final)
if final == 10:
    print("perfección")
elif final >= 6:
    print("aprobado")
else:
    print("reprobado")