import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

dados = [
    ('Maria', 54),
    ('Betânia', 25),
    ('Julia', 23),
    ('Carlos', 18),
    ('João', 32),
    ('Pedro', 15)
]

cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", dados)

conn.commit()
cursor.close()
conn.close()