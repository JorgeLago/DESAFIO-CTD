#Faça um programa que leia nome e idade e imprima quando o usuário irá completar 100 anos.
nome=input('Qual o seu nome ?:' )
idade=int(input('Qual a sua idade?: '))
idade_futura=100-idade
ano_futuro=idade_futura+2022
print('{} completará 100 anos, daqui a {} anos, em {}.'.format(nome, idade_futura, ano_futuro))