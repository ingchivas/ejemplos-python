f1 = input()
f2 = input()
n = int(input()) #la n es la posición de la serie que quiero sacar con la regla de Fibonacci
if n==1:
    print(f1)
elif n==2:
    print(f2)
else: 
    for i in range (3, n+1): #Toma todo lo que hay desde el 3 hasta el n+1(ej:3.9999)
        aux = str(f1) + str(f2)
        f1=f2
        f2=aux
    print(f2)