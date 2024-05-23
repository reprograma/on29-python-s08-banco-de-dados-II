"""1. **Criação do Banco de Dados e Tabela**
    - Crie um banco de dados SQLite chamado `livraria.db`.
    - Crie uma tabela chamada `livros` com as colunas:
        - `id` (INTEGER, chave primária, autoincremento)
        - `titulo` (TEXT)
        - `autor` (TEXT)
        - `ano` (INTEGER)
        - `preco` (REAL)"""

import sqlite3

conn = sqlite3.connect('livraria.db') # conexão 
cursor = conn.cursor() # criar o cursor para usar dentro do sqlite

# comandos SQL para criação da tabela
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
cursor.close()
conn.close()