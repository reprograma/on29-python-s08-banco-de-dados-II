import sqlite3

#conexão
conn = sqlite3.connect("escola.db")
#colocar os comandos sql
cursor = conn.cursor()

#colocar os comandos SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)

""")


# commit a informação
conn.commit()

# fechar a conexão
cursor.close()
conn.close()
