#4. **Atualização de Dados**
#    - Escreva um script Python que atualize o preço de um livro específico (por exemplo, mude o preço do livro com `id` 1 para 29.99).

import sqlite3

conn = sqlite3.connect("livraria.db")
cursor = conn.cursor()

id = input("Digite a id do livro que deseja atualizar o preço: ")
preco = input("Digite o novo preço do livro: ")

cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (preco, id))

conn.commit()
cursor.close()
conn.close()