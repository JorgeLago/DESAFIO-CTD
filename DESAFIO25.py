#Faça um programa que leia uma frase pelo teclado e mostre:
#a) quantas vezes aparece a letra  "a".
#b) em que posição ela aparece a primeira vez.
#c) em que posição ela aparece a ultima vez.
frase=str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes.'.format(frase.count('A')))

print('A primeira vez na posição {}'.format(frase.find('A')))
#método Rfind -> retorna posição de trás para frente.
print('A última vez na posição {}'.format(frase.rfind('A')))