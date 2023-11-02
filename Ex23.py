contador=1
lista1=[]
lista2=[]
igual=0

while contador<5:
    lista1.append(input("Introduz um número na Lista 1 "))
    lista2.append(input("Introduz um número na Lista 2 "))
    contador+=1

set1=set(lista1)
set2=set(lista2)
igual=list(set1.intersection(set2))

print(len(igual)
      , " números iguais")
