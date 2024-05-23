#Crie um script que selecione e exiba todos os registros da tabela estudantes.

import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM estudantes")
registros = cursor.fetchall()

for registro in registros:
    print(registro)

#EXTRA: crie um script que pergunte um nome ao usuário, selecione e exiba todos os registros com esse nome.

nome = input("Insira o nome que deseja consultar: ")

cursor.execute("SELECT * FROM estudantes WHERE nome = ?", (nome,)) 
#a vírgula após a variável/argumento é necessária por motivos de sintaxe

registros = cursor.fetchall()

for registro in registros:
    print(registro)

#no uso exclusivo do SELECT, não é necessário commitar, pois é apenas uma consulta de dados, não uma atualização
cursor.close()
conn.close()