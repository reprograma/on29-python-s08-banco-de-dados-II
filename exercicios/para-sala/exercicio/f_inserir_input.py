import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

nome = input("Digite um nome: ")
idade = input("Digite a idade: ")

cursor.execute("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", (nome, idade))

conn.commit()
cursor.close()
conn.close()