
n1=float(input("Primeiro número para calcular: "))
simb=input("Introduz a operação que deseja fazer: ")
n2=float(input("Segundo Número para calcular: "))

match simb:
    case '+':
        print("O resultado é: ", n1+n2)
    case '-':
        print("O resultado é: ", n1-n2)
    case '*':
        print("O resultado é: ", n1*n2)
    case '/':
        print("O resultado é: ", n1/n2)
