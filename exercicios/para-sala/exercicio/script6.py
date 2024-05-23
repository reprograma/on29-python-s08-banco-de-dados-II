#Escreva um script que selecione e exiba todos os estudantes cuja idade seja maior que 21.

import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM estudantes WHERE idade > 21")
registros = cursor.fetchall()

for registro in registros:
    print(registro)

cursor.close()
conn.close()