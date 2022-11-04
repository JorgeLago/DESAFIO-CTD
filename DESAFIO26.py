#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#ex.: Ana Maria de Souza
#primeiro=Ana
#último=Souza
frase=str(input('Digite seu nome completo: ')).title().split()
print('Seu primeiro nome é {}'.format(frase[0]))
print('Seu ultimo nome é {}'.format(frase[-1]))