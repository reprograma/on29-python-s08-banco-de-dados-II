import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

nome = input("Digite um nome: ")

cursor.execute("SELECT nome FROM estudantes WHERE nome = ? ", (nome,))
registros = cursor.fetchall()

for registro in registros:
       print(registro)

cursor.close()
conn.close()