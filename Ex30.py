import random 

lista=[]
pares=0
impares=0

for i in range (0,20):
    lista.append(random.randrange(1,100))
    if (lista[i]%2==0):
        pares+=lista[i]
    else:
        impares+=lista[i]

print("Lista: ", lista)
print("Soma dos números pares: ", pares)
print("Soma dos números impares: ", impares)
