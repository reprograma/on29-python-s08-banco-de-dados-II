#1. Criar banco de dados "livraria.db"

import sqlite3

conn = sqlite3.connect("livraria.db")
cursor = conn.cursor()

cursor.execute("""
                 CREATE TABLE IF NOT EXISTS livros (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 titulo TEXT NOT NULL,
                 autor TEXT NOT NULL,
                 ano INTEGER NOT NULL,
                 preco REAL NOT NULL
                 )
                """)

conn.commit()
cursor.close()
conn.close()