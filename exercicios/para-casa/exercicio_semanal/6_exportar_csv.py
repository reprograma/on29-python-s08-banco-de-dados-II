import sqlite3
import csv

conn = sqlite3.connect("livraria.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
livros = cursor.fetchall()

with open ('livros_exportados.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(livros)

cursor.close()
conn.close()