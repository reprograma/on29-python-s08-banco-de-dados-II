#Crie um script que leia o arquivo CSV 'produtos.csv' e exiba seu conteúdo no terminal.

import csv

with open('produtos.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)