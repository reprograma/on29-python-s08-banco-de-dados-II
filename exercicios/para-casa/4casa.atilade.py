import sqlite3

# ID do livro que será atualizado
livro_id = 1
novo_preco = 29.99

# Conexão com o banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Atualização do preço do livro com o ID especificado
cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, livro_id))

# Confirma as mudanças
conn.commit()

# Verifica se a atualização foi bem-sucedida
cursor.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
livro_atualizado = cursor.fetchone()
print(f"Livro atualizado: ID: {livro_atualizado[0]}, Título: {livro_atualizado[1]}, Autor: {livro_atualizado[2]}, Ano: {livro_atualizado[3]}, Preço: {livro_atualizado[4]}")

# Fecha a conexão
cursor.close()
conn.close()
