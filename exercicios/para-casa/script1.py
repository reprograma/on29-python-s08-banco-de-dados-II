import csv
import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

with open ('livros.csv', mode='r', newline= '', encoding='utf-8') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        cursor.execute(''' INSERT INTO livros(titulo, autor, ano,preco)
                       VALUES (?, ?, ?, ?)''', (linha['titulo'], linha['autor'], linha['ano'], linha ['preco']))

conn.commit()
conn.close()
