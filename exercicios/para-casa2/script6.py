"""5. **Remoção de Dados**
    - Escreva um script Python que remova um livro específico da tabela
    (por exemplo, remova o livro com `id` 3)."""

import sqlite3

conn = sqlite3.connect('livraria.db') # conexão 
cursor = conn.cursor() # criar o cursor para usar dentro do sqlite

cursor.execute("DELETE FROM livros WHERE id = 6") # direciona o cursor para execução do comando SQL


cursor.execute("SELECT * FROM livros")
livros_atualizados = cursor.fetchall()

# Imprimir a lista atualizada de livros
print("Lista atualizada de livros:")
for livro in livros_atualizados:
    print(livro)


conn.commit()
cursor.close()
conn.close()