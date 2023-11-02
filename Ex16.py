i=1
par=0
impar=0

while (i!=0):
    i=int(input("Introduza um número: (sair no 0) - "))
    if (i==0):
        break
    if (i%2==0):
        par += 1
    else:
        impar += 1

print("Números pares: ", par)
print("Números ímpares: ",impar)