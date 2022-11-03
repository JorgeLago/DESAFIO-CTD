#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados:
#ex.:
#numero: 1834
#unid: 4
#dezena:3
#centena:8
#milhar:1

numero=int(input('Digite o número: '))

if numero<10:
    numero=str(numero)
    print('Unidade: ',numero[0])
    print('Dezena 0')
    print('Centena 0')
    print('Milhar 0')
elif numero<100:
    numero=str(numero)
    print('Unidade: ',numero[1])
    print('Dezena ', numero[0])
    print('Centena 0')
    print('Milhar 0')
elif numero<1000:
    numero=str(numero)
    print('Unidade: ',numero[2])
    print('Dezena ', numero[1])
    print('Centena ', numero[0])
    print('Milhar 0')
elif numero<10000:
    numero=str(numero)
    print('Unidade: ',numero[3])
    print('Dezena ', numero[2])
    print('Centena ', numero[1])
    print('Milhar ', numero[0])
    
else:
    print('Precisa ser entre 0 e 9999.') 