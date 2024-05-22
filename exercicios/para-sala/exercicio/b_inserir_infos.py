import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

#lista com informações para a tabela
estudantes = [
    ('Alice', 21),
    ('Bob', 22),
    ('Charlie', 23)
]
#inserir várias informações na tabela de uma só vez
cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

conn.commit()
cursor.close()
conn.close()