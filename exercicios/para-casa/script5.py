import sqlite3

conn =sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("update livros set preco = ? where id = ?", (28.70,12))

conn.commit()
cursor.close()
conn.close()