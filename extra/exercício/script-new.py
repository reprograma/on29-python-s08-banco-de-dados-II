import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

# Criando as tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
""")
# Inserindo dados
cursor.executemany("INSERT INTO clientes (nome) VALUES (?)", [
    ('João',),
    ('Maria',),
    ('Pedro',)
])
cursor.executemany("INSERT INTO pedidos (cliente_id, produto, quantidade) VALUES (?, ?, ?)", [
    (1, 'Produto A', 2),
    (2, 'Produto B', 3),
    (3, 'Produto C', 1),
    (1, 'Produto D', 5)
])
conn.commit()