import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

livros = [
    ('A', 'João', 2020, 25.99),
    ('B','Maria', 2019, 19.99),
    ('C', 'José', 2018, 29.99),
    ('E', 'Marcelie', 2022, 22.99),
    ('D',  'Marcel', 2021, 15.99)
]

cursor.executemany("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", livros)

conn.commit()
cursor.close()
conn.close()

