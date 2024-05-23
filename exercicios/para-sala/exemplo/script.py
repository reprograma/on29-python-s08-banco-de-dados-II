import sqlite3

conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
    )
    """)

# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('joao', 43)")
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('kiko', 89)")


cursor.execute("SELECT * FROM usuarios")
registros = cursor.fetchall()

for registro in registros:
       print(registro)
       
conn.commit()
conn.close()
