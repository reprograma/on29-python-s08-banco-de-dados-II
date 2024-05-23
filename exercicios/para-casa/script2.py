import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
registros = cursor.fetchall()
for registro in registros:
    print(registro)


conn.close()