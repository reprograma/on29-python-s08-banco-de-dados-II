import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (29.99, 1))

conn.commit()
cursor.close()
conn.close()