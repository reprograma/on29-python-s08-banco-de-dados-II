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

# Executa instrução SQL
# inseri, atualiza ou deleta múltiplos registros de uma só vez, 
# É utilizado para não fazer isso um por um com várias chamados ao 'cursor.execute()'.
cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", dados)

conn.commit()
cursor.close()
conn.close()