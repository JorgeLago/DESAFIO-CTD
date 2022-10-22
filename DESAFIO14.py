
#Faça um programa que leia um número e imprima se ele é par ou ímpar.
num=int(input('Digite um número: '))
resto=(num % 2)
if resto == 0:
    print('O número é par')
else:
    print('O número é ímpar')