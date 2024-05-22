import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()
id = input("ID:")
preco = input ("novo preço: ")

cursor.execute("UPDATE livros SET preco= ? WHERE id = ?", (preco, id))

conn.commit()
cursor.close()
conn.close()