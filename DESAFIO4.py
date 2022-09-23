#Faça um programa que recea duas dimensões de terreno (frente e fundo) e imprima a área deste terreno. Considerando que o preço do metro quadrado é de R$7.592,00, imprima também o valor que custará este terreno.
from decimal import Decimal
import locale
from unicodedata import decimal
locale.setlocale(locale.LC_ALL, 'pt_BR')
metro_quadrado_preco=float(7592.00)
largura=float(input("Qual a medida de largura ?  "))
comprimento=float(input("Qual a medida de comprimento ?  "))
area_terreno=(largura*comprimento)
preco_terreno= float(metro_quadrado_preco*area_terreno)
print("A area do terreno é ",area_terreno, "metros quadrados e custará um total de R$ ",locale.currency(preco_terreno,grouping=True), "reais.")