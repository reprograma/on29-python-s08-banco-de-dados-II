import csv
import sqlite3

# Conectar ao banco de dados (ou criar um novo banco se não existir)
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Criar a tabela se ela não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    preco REAL NOT NULL
)
''')

# Ler os dados do arquivo CSV
with open('livros.csv', mode='r', encoding='utf-8') as file:
    leitor = csv.DictReader(file)
    livros = [(row['titulo'], row['autor'], int(row['ano']), float(row['preco'])) for row in leitor]

# Inserir os dados na tabela
cursor.executemany('''
INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)
''', livros)

# Confirmar as mudanças
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

# Fechar Cursor
