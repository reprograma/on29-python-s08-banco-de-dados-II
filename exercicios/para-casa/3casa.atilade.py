import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Seleciona todos os registros da tabela 'livros'
cursor.execute("SELECT * FROM livros")

# Recupera todos os resultados
livros = cursor.fetchall()

# Exibe os registros
for livro in livros:
    print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Preço: {livro[4]}")

# Fecha a conexão
cursor.close()
conn.close()
