# Escreva um script Python que remova um livro específico da tabela (por exemplo, remova o livro com `id` 3).
import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("""
   DELETE FROM livros 
   WHERE id = ?
               """, (1,))

conn.commit()
print('Livro removido com sucesso!')


conn.close()