#Faça um programa que receba uma string de letras repetidas e imprima a quantidade de cada letras, caso passe de 9, reiniciar a contagem em outro elemento.

string = "BBBBBBBBBBBBBAACCCDD"
# numero=0
# letra=''
# lista=[]

# for idx, char in enumerate(string):
#     if idx == 0:
#         letra=char
#         numero += 1
#     else:
#         if numero<=8:
#             if char==letra:
#                 numero+=1
#             else:
#                 lista.append(str(numero)+letra)
#                 letra=char
#                 numero=1
#         else:
#             lista.append(str(numero)+letra)
#             letra=char
#             numero=1

# print(lista)
lista=[]
for letra in string:
    while elemento not in lista:
        numero=string.count(letra)
        letras=letra
        elemento=lista.append(str(numero)+letras) 

print(lista)