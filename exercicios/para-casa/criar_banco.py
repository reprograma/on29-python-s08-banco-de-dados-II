# Importa a biblioteca sqlite3 
# Cria e abrir conexão com banco de dados 
# Cria um cursor
# Criar uma tabela 
# Confirma , commit.
# Fecha a conexão com o banco de dados


import sqlite3

conn = sqlite3.connect('livraria.db')


cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,   
        titulo TEXT,                           
        autor TEXT,                           
        ano INTEGER,                          
        preco REAL                             
    )
''')


conn.commit()


conn.close()


print("Arraso está ai seu Banco de dados!")