import csv
import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def importar_csv():
  with open('livros.csv', 'r') as livros_csv:
    leitor = csv.reader(livros_csv)
    next(leitor)
    for linha in livros_csv:
      cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", linha.split(','))

  conn.commit()



