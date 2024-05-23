#Faça um script que exporte os dados da tabela clientes de empresa.db para um arquivo chamado exportados_clientes.csv.

import sqlite3
import csv

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
dados = cursor.fetchall()

with open('exportados_clientes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'email'])
    escritor.writerows(dados)

conn.commit()
cursor.close()
conn.close()