# Um novo modelo de carro, super econômico foi lançado.
# Ele faz 20 km com 1 litro de combustível.
# Cada litro de combustível custa R$ 5,00.

# Faça um programa que pergunte ao usuário quanto de dinheiro ele tem e em seguida diga quantos litros de combustível ele pode comprar
#  e quantos kilometros o carro consegue andar com este tanto de combustível.

dinheiro = float(input(' Quanto de dinheiro você vai colocar?: R$'))
qntd_combustivel = float(dinheiro/5)
km_rodados = qntd_combustivel*20
print('Com ',dinheiro , 'você irá comprar um total de ',qntd_combustivel , 'litros de combustível e rodará um total de ',km_rodados , 'kms.')