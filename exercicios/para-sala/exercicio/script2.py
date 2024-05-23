import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

nome = input("digite um nome: ")

cursor.execute("SELECT * FROM estudantes WHERE nome = ? ", (nome,))
registros = cursor.fetchall()

for registro in registros:
    print(registro)

cursor.close()
conn.close()