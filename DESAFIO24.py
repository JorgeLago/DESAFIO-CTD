#Crie um programa que leia o nome de uma pessoa, e diga se tem "silva" no nome.
nome=str(input('Digite seu nome completo: '))
if ('silva' in nome.lower()):
    print('Seu nome contem silva.')
else:
    print('Seu nome não contem silva.')