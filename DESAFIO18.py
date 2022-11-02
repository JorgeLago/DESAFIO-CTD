#Crie um programa que leia um número Real qualquer pelo teclado e na tela a sua porção inteira.
#Ex.: Digite um número: 6.127 / O numero 6.127 tem a parte inteira 6.
from math import trunc
numero = float(input('Digite o número Real: '))
print(trunc(numero))