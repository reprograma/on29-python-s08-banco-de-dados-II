import sqlite3


#EXPLICAÇÃO DOS COMANDOS

#conexão
conn = sqlite3.connect("exemplos.db")
#criar o cursor para uso do SQL
cursor = conn.cursor()

#colocar os comandos SQL
cursor.execute("""
   CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
    )
    """)
#inserir os dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('João', 43)")
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Flávia', 29)")

#selecionar os dados inseridos
cursor.execute("SELECT * FROM usuarios")
#buscar as informações
registros = cursor.fetchall()

#printar as informações
for registro in registros:
    print(registro)
#commita a informação
conn.commit()
#fechar a conexão
cursor.close()
conn.close()
