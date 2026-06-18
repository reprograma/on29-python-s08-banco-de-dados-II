import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def remover_livro():
  cursor.execute("DELETE FROM livros WHERE id = ?", (2,))
  conn.commit()