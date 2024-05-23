# Importar a biblioteca sqlite3 
# Abrir conexão com banco de dados
# Criar um cursor
# Selecionar todos os registros da tabela 'livros'
# Pegar os registros 
# for in
# Imprimir o registro
# Fechar a conexão 

import sqlite3 

conn = sqlite3.connect('livraria.db')

cursor = conn.cursor()


cursor.execute('SELECT * FROM livros')

rows = cursor.fetchall()


for row in rows:
    
    print(row)


conn.close()

