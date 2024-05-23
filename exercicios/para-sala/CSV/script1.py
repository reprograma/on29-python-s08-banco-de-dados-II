"""7. **Leitura de CSV**:
   - Crie um script que leia um arquivo CSV chamado `produtos.csv` contendo as colunas `id`, `nome` e `preco`, e exiba seu conteúdo no terminal.
"""
  
import csv

with open('produtos.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)    