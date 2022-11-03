#Faça um programa que leia o nome completo de uma pessoa e mostre:
#a) nome com todas as letras maiusculas:
#b) nome com todas minúsculas:
#c)quantas letras ao todo ( sem considerar espaços):
#d)quantas letras tem o primeiro nome:

nome_completo = str(input('Qual seu nome completo? >'))
print(nome_completo.upper())
print(nome_completo.lower())
print('possui ', len(nome_completo.strip()), 'espaços, desconsiderando espaços.')
nome_completo=(nome_completo.split(' '))
print('O seu primeiro nome possui', len(nome_completo[0]), 'letras.')