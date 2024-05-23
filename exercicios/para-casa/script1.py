import sqlite3

# Conectar ao banco de dados (ou criar um novo banco se não existir)
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Criar uma tabela para armazenar os livros
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    preco REAL NOT NULL
)
''')

#fechar comit
conn.commit()
#fechar cursor
conn.close()