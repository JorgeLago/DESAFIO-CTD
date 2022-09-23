#Faça um programa que receba 4 notas de um aluno, uma de cada bimestre, e calcule a média final. Imprima a média final e se o aluno foi APROVADO ou REPROVADO, considerando que a média de aprovação seja maior/igual a 6.

media_aprovacao=6
Nota1=float(input("digite a nota primeiro bimestre: "))
nota2=float(input("digite a nota segundo bimestre: "))
nota3=float(input("digite a nota terceiro bimestre: "))
nota4=float(input("digite a nota quarto bimestre: "))

media_final = (Nota1+nota2+nota3+nota4)/4
if media_final>=media_aprovacao:
    print("O Aluno está aprovado com média ",media_final)
else:
    print("O Aluno está reprovado com média ",media_final)