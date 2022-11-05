#ler um número e multiplicar seus elementos.
import sys
import math

num = (input('digite um numero: '))
lista=[]
for i in num:
    i=int(i)
    lista.append(i)
    resultado=math.prod(lista)

print(resultado)