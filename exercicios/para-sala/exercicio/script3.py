import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()
nome = input("Nome: ")
idade = input("Idade: ")

cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (idade, nome))

conn.commit()
cursor.close()
conn.close()
