import sqlite3

conn = sqlite3.connect("livraria.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM livros WHERE titulo = ?", ('Aurora',))

conn.commit()
cursor.close()
conn.close()
