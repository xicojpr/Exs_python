pal = input("Introduz uma palavra: \n")


vogais='AEIOUaeiou'
consuantes='BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
count=0
countc=0

for letra in pal:
    if letra in vogais:
        count=count+1
    elif letra in consuantes:
        countc+=1

print(count, " vogais")
print(countc, " consuantes")
    
