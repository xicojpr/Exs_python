valor=int(input("Introduza um número- \n"))

res=1
count=1

while count <= valor:
    res *= count
    count += 1

print(res)