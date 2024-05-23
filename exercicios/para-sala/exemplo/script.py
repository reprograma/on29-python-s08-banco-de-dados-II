import sqlite3

conn = sqlite3.connect("exemplo.db") #como o database ainda não existia, ao rodarmos o programa, ele será criado
cursor = conn.cursor() #criando um cursor para interagir com o SQL

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL 
    )""") 
#criou-se a tabela usuarios (caso já não existisse) com colunas id, nome e idade (que não aceitam valores vazios)

#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('João', 18)")
#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Maria', 19)")

cursor.execute("SELECT * FROM usuarios")

registros = cursor.fetchall() #guardando aquilo selecionado com o SELECT na variável "registros"

for registro in registros:
    print(registro)

conn.commit() #executará de fato aquilo apontado nos executes

conn.close() #fechando a conexão