#Escreva um programa que leia  velocidade de um carro.  Se ele ultrapassar 80km/h, 
# mostre uma mensagem dizendo que ele foi multado.  
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade=float(input('Qual a velocidade do carro? > '))
if velocidade>80:
    print('Você ultrapassou a velocidade permitida com {} km/h, e o valor da sua multa vai custar R${}.'.format(velocidade, float((velocidade-80)*7.00)))
else:
    print('Você está dentro do limite, Parabéns!')