#Faça um programa que leia 3 numeros inteiros e imprima o maior e o menor deles.

def maior(numero1,numero2,numero3):
    max = numero1

    if numero2>max:
        max=numero2
    if numero3>max:
        max=numero3
    return max

def menor(numero1,numero2,numero3):
    min=numero1
    if numero2<min:
        min=numero2
    if numero3<min:
        min=numero3   
    return min

numero1= int(input("digite o primeiro numero: "))
numero2= int(input("digite o segundo numero: "))
numero3= int(input("digite o terceiro numero: "))

print("Maior: ", maior(numero1,numero2,numero3))
print("Menor: ", menor(numero1,numero2,numero3))