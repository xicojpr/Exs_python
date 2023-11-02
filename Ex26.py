import random
numero=random.randint(1,100)
tentativas=3
i=1

while (i<4 and tentativas!=numero):
    adv=int(input("Adivinha o número de 1 a 100 \n"))
    if adv==numero:
        print("Acertaste!!")
        break
    else:
        i+=1
        print("Falhas-te aldrabão")
    if (adv<numero):
        print("Número mais alto ")
    else:
        print("Número mais baixo")
    if (i==3):
        print("Falhas-te as 3 tentativas")

