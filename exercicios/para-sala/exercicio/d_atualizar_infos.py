import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

nome = input("Digite um nome: ")
idade = input("Digite a idade: ")
id = input("Digite o id: ")

cursor.execute("UPDATE estudantes SET nome = ?, idade = ? WHERE id = ?", (nome, idade, id))

conn.commit()
cursor.close()
conn.close()