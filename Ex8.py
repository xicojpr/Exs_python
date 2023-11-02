print("Calculo da média ")
teste= float(input("Introduz a nota do teste \n"))
trab= float(input("Introduz a nota do trabalho \n"))

med=0.6*teste+0.4*trab

if (med<9.5):
    print("Reprovado com: ",med)
else :
    print("Aprovado com : ",med)