def soma():
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    print("Soma: ",num1+num2)

def subtracao():
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    print("Subtração: ",num1-num2)

def multiplicacao():
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    print("Multiplicação: ",num1*num2)

def divisao():
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    print("Divisão: ",num1/num2)

    
opcao=1

while opcao:
   
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão ")
    print("0. Sair")

    opcao = int(input("Opção: "))

    if(opcao==1):
        soma()
        print("Operação realizada com sucesso!")
    if(opcao==2):
        subtracao()
        print("Operação realizada com sucesso!")
    if(opcao==3):
        multiplicacao()
        print("Operação realizada com sucesso!")
    if(opcao==4):
        divisao()
        print("Operação realizada com sucesso!")
    if(opcao>=5):
      
        print("Está opção não existe.")