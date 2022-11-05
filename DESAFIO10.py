#Faça um programa que leia dois números e imprima:
#a) A soma dos 2 numeros,
#b) O produto do primeiro número pelo quadrado do segundo,
#c) O quadrado do primeiro número,
#d) A raiz quadrada da soma dos quadrados,
#e) O seno da diferença do primeiro número pelo segundo,

primeiro_numero=int(input("Digite o primeiro número: "))
segundo_numero=int(input("Digite o segundo número: "))

print("A soma dos números é {}".format(primeiro_numero+segundo_numero))
print("O produto do 1º pelo quadrado do segundo é {} ".format(primeiro_numero*(segundo_numero**2)))
print("O quadrado do primeiro número: {}".format(primeiro_numero**2))
print("A raiz quadrada da soma dos quadrados é: {}".format(((primeiro_numero**2)+(segundo_numero**2))**0,5))