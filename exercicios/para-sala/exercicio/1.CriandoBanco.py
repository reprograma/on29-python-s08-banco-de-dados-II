import sqlite3
# Conexão
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Execução dos comandos SQL
cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )              
""")

conn.commit()
conn.close()