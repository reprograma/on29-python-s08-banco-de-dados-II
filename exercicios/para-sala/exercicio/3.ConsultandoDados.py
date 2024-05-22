# Crie um script que selecione e exiba todos os registros da tabela `estudantes`.

import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

nome = input("Digite o nome que deseja consultar: ")

cursor.execute("SELECT nome FROM estudantes WHERE nome = ?", (nome, ))
registros = cursor.fetchall()
for registro in registros:
    print(registro)
    
cursor.close()
conn.close()





# (1, 'Maria', 18,) == 'Maria'