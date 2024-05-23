import sqlite3

conn = sqlite3.connect('escola.db') # conexão
cursor = conn.cursor() # criar o cursor para usar dentro do sqlite

estudantes = [
    ('Pam', 29),
    ('Edu', 22),
    ('Tai', 29),
    ('Betania', 29),
    ('Atiladê', 29)
]

cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

conn.commit()
cursor.close() # fechar o cursos trabalhando dentro do sqlite
conn.close() # encerrar conexão com o sqlite