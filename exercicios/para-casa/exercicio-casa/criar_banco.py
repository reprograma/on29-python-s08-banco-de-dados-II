# 1.**Criação do Banco de Dados e Tabela**

import sqlite3
import csv

conn = sqlite3.connect("livraria.db")
cursor = conn.cursor()

cursor.execute("""
               
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    preco REAL
)         
""")

conn.commit()
conn.close()