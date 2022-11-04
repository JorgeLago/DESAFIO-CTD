#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

numero_aleatorio=random.randrange(0,5)
numero_usuario=int(input('Digite um numero: '))
if numero_usuario==numero_aleatorio:
    print(' Você acertou, o número é {}'.format(numero_aleatorio))
else:
    print('Você Errou!!')