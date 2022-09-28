#Faça um programa que leia 3 numeros inteiros e imprima o maior e o menor deles.

def maior(num1,num2,num3):
    max = num1

    if num2>max:
        max=num2
    if num3>max:
        max=num3
    return max

def menor(num1,num2,num3):
    min=num1
    if num2<min:
        min=num2
    if num3<min:
        min=num3   
    return min

numero1= int(input("digite o primeiro numero: "))
numero2= int(input("digite o segundo numero: "))
numero3= int(input("digite o terceiro numero: "))

print("Maior: ", maior(numero1,numero2,numero3))
print("Menor: ", menor(numero1,numero2,numero3))