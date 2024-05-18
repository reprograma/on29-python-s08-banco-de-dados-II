import sqlite3

    # conexão 
conn = sqlite3.connect('escola.db')
    # criar o cursor para uso do SQL
cursor = conn.cursor()

    # colocar os comando SQL
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