import csv
import sqlite3


conn = sqlite3.connect("livraria.db")
cursor = conn.cursor()

#leitor do CSV:
with open ('livros.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)


#inserção de dados na tabela livros (livraria.db):
with open ('livros.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)
    for linha in leitor:
        cursor.execute('INSERT INTO livros (id, titulo, autor, ano, preco) VALUES (?, ?, ?, ?, ?)', (linha [0], linha[1], linha[2], linha [3], linha[4]))

conn.commit()
cursor.close()
conn.close()