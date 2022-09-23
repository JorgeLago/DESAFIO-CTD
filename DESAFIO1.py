#Faça um Programa que entre o preço de um produto e o valor em dinheiro pago. imprima para o usuário o quanto será o troco.


valor = float(input("digite o valor do produto. R$"))

pago = float(input("digite o valor pago. R$"))

troco = round(float(pago - valor))

print('o troco será de R$',troco," .")