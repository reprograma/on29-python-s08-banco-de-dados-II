#Exercício 1: crie um script Python que crie um banco de dados SQLite chamado escola.db. Em seguida, crie uma 
#tabela chamada estudantes com as colunas id, nome e idade.

import sqlite3

conn = sqlite3.connect("escola.db") #conexão com o database (que como não existia será criado)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL 
    )""") 

conn.commit()
cursor.close()
conn.close()