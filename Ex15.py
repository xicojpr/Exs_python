valor=int(input("Introduza o número de alunos: \n"))
medt=0
negteste=0
posteste=0
negtrab=0
postrab=0
for i in range (1, valor+1):
    print("Calculo da média do aluno ", i)
    teste= float(input("Introduz a nota do teste \n"))
    trab= float(input("Introduz a nota do trabalho \n"))
    meda=0.5*teste+0.5*trab
    if (teste<=9.5):
        negteste+=1
    else:
        posteste+=1
    if (trab<=9.5):
        negtrab+=1
    else:
        postrab+=1



    medt+=meda
    print("Testes- ", posteste, " positivas ", negteste, " negativas \n")
    print("Testes- ", postrab, " positivas ", negtrab, " negativas \n")
    print("Media da turma: ",medt/i)
