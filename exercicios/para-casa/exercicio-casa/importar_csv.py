# 2.**Importação de Dados de um CSV**

import sqlite3
import csv

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("""
               
   CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    ano INTEGER,
    preco REAL NOT NULL
   )
   """)

with open('livros.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # Pular o cabeçalho
    for linha in leitor:
        cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (linha[0], linha[1], linha[2], linha[3]))

    conn.commit()
    cursor.close()
    conn.close()