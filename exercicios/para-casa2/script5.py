""""4. **Atualização de Dados**
    - Escreva um script Python que atualize o preço de um livro específico (por exemplo, 
    mude o preço do livro com `id` 1 para 29.99)."""

import sqlite3

conn = sqlite3.connect('livraria.db') # conexão 
cursor = conn.cursor() # criar o cursor para usar dentro do sqlite

cursor.execute("UPDATE livros SET preco = 65.90 WHERE id = 4") # direciona o cursor para execução do comando SQL
cursor.execute("SELECT * FROM livros")

livros_atualizados = cursor.fetchall()
print("Lista atualizada de livros:")

for livro in livros_atualizados:
    print(livro)

conn.commit()
cursor.close()
conn.close()