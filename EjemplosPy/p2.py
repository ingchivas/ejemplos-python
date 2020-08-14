f1 = input()
f2 = input()
n = int(input())
if n==1:
    print (f1)
elif n==2:
    print (f2)
else:
    for i in range (3, n+1):
        aux = str(f1) + str(f2)
        f1 = f2
        f2 = aux
    print (f2)