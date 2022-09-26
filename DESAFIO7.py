#Faça um programa que leia o peso e a altura de uma pessoa e calcule o IMC dela, imprimindo o valor calculado e em qual faixa essa pessoa se encontra.

peso=float(input("Qual o peso?: "))
altura=float(input("Qual a sua altura?: "))
imc=float((peso)/(altura**2))
if imc<18.5:
    print("O Seu IMC está ",imc, "e está na faixa da magreza.")

elif 18.5<=imc<25.0:
    print("O Seu IMC está ",imc, "e está na faixa do Normal.")

elif 25.0<=imc<30.0:
    print("O Seu IMC está ",imc, "e está na faixa do Sobrepeso.")

elif 30.0<=imc<40.0:
    print("O Seu IMC está ",imc, "e está na faixa da Obesidade.")

else:
    print("O Seu IMC está ",imc, "e está na faixa da Obesidade Grave.")