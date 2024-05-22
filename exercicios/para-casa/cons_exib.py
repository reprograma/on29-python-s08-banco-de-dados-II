import sqlite3

conn = sqlite3.connect('livraria.db') # cria a conexão com o banco de dados
cursor = conn.cursor() # cria o cursor para andar dentro do db

cursor.execute("SELECT * FROM livros")
livros = cursor.fetchall()

for livro in livros:
    print(livro)

cursor.close()
conn.close()