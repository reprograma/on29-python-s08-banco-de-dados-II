# 6.**Exportação de Dados para CSV**
#- Escreva um script Python que exporte os dados da tabela `livros` para um novo arquivo CSV chamado `exportados_livros.csv`.

import sqlite3
import csv

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
dados = cursor.fetchall()

with open('exportados_livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(dados)

cursor.close()
conn.close()
