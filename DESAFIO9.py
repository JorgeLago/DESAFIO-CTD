#Faça um programa que leia a quantidade de fias traalhados pelo funcionário e imprima essa informação convertida em anos, meses e dias. considere que todos os meses possuem sempre 30 dias, à fim de simplificação.

dias_trabalhados = int(input("QUantos dias o empregrado trabalhou? :"))

anos=round(dias_trabalhados/365)
meses=dias_trabalhados/30

print("O Empregado trabalhou um total de {} Anos, {} Meses e {} Dias.".format (anos, meses, dias_trabalhados))
