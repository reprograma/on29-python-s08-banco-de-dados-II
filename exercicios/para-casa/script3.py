import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()


cursor.execute("UPDATE livros SET preco = 29.99 WHERE id = 1")
conn.commit()
conn.close()