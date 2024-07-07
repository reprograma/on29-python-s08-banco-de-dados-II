import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

titulo = input("digite o título de um livro: ")

cursor.execute(f"SELECT titulo FROM livros WHERE titulo = ? ", (titulo,))
registros = cursor.fetchall()

for registro in registros: 
        print(registro)

cursor.close()
conn.close()