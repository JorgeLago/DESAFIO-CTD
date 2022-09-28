# Faça um programa que recebe o valor dos catetos de um triangulo e imprima na tela o valor da hipotenusa. Lembre-se que: h² = a²+b², sendo h - hipotenusa a e b- catetos do triângulo.
catetoa=int(input("Valor do primeiro cateto: "))
catetob=int(input("Valor do segundo cateto: "))
hipotenusa=int(catetoa*catetob)/2
print("A hipotenusa desse triângulo é ",hipotenusa )