import sqlite3
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
    )
    """)


"""#inserir dois usuário na tabela exemplo db
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Pam', 29) ")
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('kiko', 89) ")"""

#pegar todos os dados? da tabela exemplo db
cursor.execute("Select * FROM usuarios")
registros= cursor.fetchall()

for registro in registros:
    print(registro)

# essas duas linhas seguintes são importantes de estarem presentes no final do codigo pq:
conn.commit() # Commit informa as alterações feitas na tabela
conn.close() # para fechar a conexão iniciada (boa prática)