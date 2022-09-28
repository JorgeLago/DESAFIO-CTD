#Faça um programa que receba um número inteiro positivo N e calcule o somatório de 1 até N. Imprima na tela o resultado da soma.

numero=int(input("digite um numero:  "))
soma=0
for i in range(1,numero+1):
    soma+=i
print("O resultado da soma de 1 até "+str(numero) + " é " + str(soma))