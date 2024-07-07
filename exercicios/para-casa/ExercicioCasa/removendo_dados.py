import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

titulo = 'D'

cursor.execute("DELETE FROM livros WHERE titulo = ?", (titulo,))

conn.commit()
cursor.close()
conn.close()