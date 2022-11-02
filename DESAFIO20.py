# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
nomes = []
alunos=0
quantidade=int(input('Quantos alunos na lista?' ))

while alunos<quantidade:
    nome=str(input('Digite o nome: '))
    nomes.append(nome)
    alunos +=1
    
#método do random para misturar elementos.
random.shuffle(nomes)
print(nomes)