import sqlite3

conn = sqlite3.connect ("livraria.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL, 
    ano TEXT NOT NULL,
    preço REAL           
    )
               """)

conn.commit()
cursor.close()
conn.close()
