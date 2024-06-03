#5. **Remoção de Dados**
#    - Escreva um script Python que remova um livro específico da tabela (por exemplo, remova o livro com `id` 3).
import sqlite3

conn = sqlite3.connect("livraria.db")
cursor = conn.cursor
()

id = input("Digite a id do livro que deseja remover: ")
titulo = input("Confirme sua escolha digitando o título do livro que deseja remover: ") #pedi o título pra evitar que o usuário delete o livro com a id errada.

cursor.execute("DELETE FROM livros WHERE id = ? and titulo = ?", (id, titulo))

conn.commit()
cursor.close()
conn.close()