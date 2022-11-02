# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele. lendo o nome deles e escrevendo o nome do escolhido.
import random
nomes = []
alunos=0
quantidade=int(input('Quantos alunos na lista?' ))

while alunos<quantidade:
    nome=str(input('Digite o nome: '))
    nomes.append(nome)
    alunos +=1

sorteado = random.choice(nomes)
print('O aluno sorteado foi ',(sorteado))