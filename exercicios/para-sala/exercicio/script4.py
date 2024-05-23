#Escreva um script que atualize a idade de um estudante específico (por exemplo, mude a idade de "Bob" para 23).

import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))

#Escreva um script que atualize os dados de um registro com base em seu id, com dados recebidos pelo usuário.

id = int(input("Insira o ID do registro que deseja atualizar: "))
nome = input("Insira o nome: ")
idade = (input("Insira a idade: "))

cursor.execute("UPDATE estudantes SET nome = ?, idade = ? WHERE id = ?", (nome, idade, id))

conn.commit()
cursor.close()
conn.close()