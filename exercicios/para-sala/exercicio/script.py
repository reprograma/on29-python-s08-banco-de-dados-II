import sqlite3

conn = sqlite3.connect('escola.db') # conexão 
cursor = conn.cursor() # criar o cursor para usar dentro do sqlite

# comandos SQL para criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")
conn.commit()
cursor.close()
conn.close()