valor=int(input("Introduza o número de alunos: \n"))
medt=0
for i in range (1, valor+1):
    print("Calculo da média do aluno ", i)
    teste= float(input("Introduz a nota do teste \n"))
    trab= float(input("Introduz a nota do trabalho \n"))
    meda=0.5*teste+0.5*trab
    medt+=meda/i
    print("A média da turma é: ", medt/valor)
