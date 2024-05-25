import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Criação da tabela 'livros'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    preco REAL NOT NULL
    )
    """)

# Inserção de dados na tabela 'livros'
cursor.executemany("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", [
    ('Porque Gritamos', 'Elizama Santos', 2023, 35.0),
    ('Escritos de uma vida', 'Sueli Carneiro', 2018, 50.0),
    ('Mitologia dos Orixas', 'Reginaldo Prandi', 2001, 80.0),
    ('Olhos Dagua', 'Conceição Evaristo', 2016, 5.0),
    ('Carta a minha filha', 'Maya Angelou', 2029, 65.0)
])

conn.commit()
conn.close()
