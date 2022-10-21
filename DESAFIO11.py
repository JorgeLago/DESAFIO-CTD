#Faça uma calculadora!
# que leia um valor, um operador (+,-,*,/) e um outro valor.
#Efetue a operação passada pelo usuário e imprima o resultado.

num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))
print("Qual a Operação deseja que seja feita?: ")
operacao=str(input("+, -, *, / ): "))
if operacao == "+":
    print("A soma resulta em {}".format(num1+num2))
if operacao == "-":
    print("A diferença resulta em {}".format(num1-num2))
if operacao == "*":
    print("A multiplicação resulta em {}".format(num1*num2))
if operacao == "/":
    print("A divisão resulta em {}".format(num1/num2))