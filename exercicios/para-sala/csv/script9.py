#Crie um script que leia o arquivo 'clientes.csv' e insira os dados numa tabela 'clientes' no database empresa.db.

import csv
import sqlite3

conn = sqlite3.connect('empresa.db') #como ainda não existe, iremos criar esse database
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

with open('clientes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor) #pulando o cabeçalho para não atribuir os nomes das coluna como dados
    for linha in leitor:
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (linha[1], linha[2]))

conn.commit()
cursor.close()
conn.close()