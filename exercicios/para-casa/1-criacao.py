import sqlite3

# 1- Criação do Banco de Dados
connection = sqlite3.connect('livraria.db')
cursor = connection.cursor()

# 2- Criar Tabela, o if not exists vai garantir que não seja criada duas vezes a mesma tabela 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER NOT NULL,
        preco REAL
        )
        """)



connection.commit() # vai ler as alterações que foram feitas no banco de dados 
cursor.close() # objeto que percorre tudo que está no banco de dados 
connection.close() # boa prática para sempre garantir o fechamento da coração 
