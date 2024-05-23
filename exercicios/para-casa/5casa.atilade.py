import sqlite3

# ID do livro que será removido
livro_id = 3

# Conexão com o banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Remoção do livro com o ID especificado
cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))

# Confirma as mudanças
conn.commit()

# Verifica se a remoção foi bem-sucedida
cursor.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
livro_removido = cursor.fetchone()
if livro_removido is None:
    print(f"O livro com ID {livro_id} foi removido com sucesso.")
else:
    print(f"Falha ao remover o livro com ID {livro_id}.")

# Fecha a conexão
cursor.close()
conn.close()
