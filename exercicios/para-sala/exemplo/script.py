import sqlite3

conn = sqlite3.connect("exemplo.db") # conect, se o arquivo não existir, ele cria e conecta. 
cursor = conn.cursor() # criando o cursor
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    
""")

"""
    # (IF NOT EXISTS usuarios ) se não existir, cria.

NOT NULL - o campo nome e o campo idade, tem que ter informação, nõ aceita nulo


"""

cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('joao', 43)")
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('kiko', 89)")

cursor.execute("SELECT * FROM usuarios")
registros = cursor.fetchall()

for registro in registros:
    print(registro)

conn.commit() #executa 
conn.close() #fecha o que abrimos 