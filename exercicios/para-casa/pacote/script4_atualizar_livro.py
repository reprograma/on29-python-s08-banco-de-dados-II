import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def atualizar_livro():
  cursor.execute("UPDATE livros SET preco = ? WHERE titulo = ?", (32.50, 'Dom Casmurro'))
  conn.commit()