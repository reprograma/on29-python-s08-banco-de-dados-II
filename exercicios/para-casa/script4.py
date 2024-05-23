import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Selecionar todos os registros da tabela livros
cursor.execute('SELECT * FROM livros')
rows = cursor.fetchall()

# Exibir os registros
print("Lista dos livros no banco de dados:")
for row in rows:
    print(f"ID: {row[0]}, Título: {row[1]}, Autor: {row[2]}, Ano: {row[3]}, Preço: R$ {row[4]:.2f}")

# Fechar a conexão com o banco de dados
conn.close()