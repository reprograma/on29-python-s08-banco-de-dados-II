import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
livros = cursor.fetchall()

for livro in livros:
    print(livro)
    
cursor.close()
conn.close()