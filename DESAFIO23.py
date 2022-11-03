#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "santo".
cidade=str(input('Digite o nome da sua cidade: '))
cidade=cidade.split(' ')
if cidade[0]=='santo':
    print('A cidade começa com a palavra santo.')
else:
    print('Não começa com a palavra santo.')