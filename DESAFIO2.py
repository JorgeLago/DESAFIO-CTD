#Faça um programa que leia 3 numeros inteiros e imprima o maior e o menor deles.

numero1= int(input("digite o primeiro numero: "))
numero2= int(input("digite o segundo numero: "))
numero3= int(input("digite o terceiro numero: "))

print("Maior: ", max(numero1,numero2,numero3))
print("Menor: ", min(numero1,numero2,numero3))