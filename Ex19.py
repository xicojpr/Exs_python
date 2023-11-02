pal = input("Introduz uma palavra: \n")


vogais='AEIOUaeiou'
count=0

for letra in pal:
    if letra in vogais:
        count=count+1

print(count, " vogais")
    
