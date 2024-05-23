import sqlite3

conn = sqlite3.connect('meu_banco_de_dados.db')
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
# Coloquei como comentario para não ficar criando esses mesmos usuarios eternamente

cursor.execute("SELECT * FROM usuarios")
registros = cursor.fetchall()

for registro in registros:
    print(registro)

conn.commit()
conn.close()
