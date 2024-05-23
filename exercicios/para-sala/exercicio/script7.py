import sqlite3


conn = sqlite3.connect('escola.db')
cursor = conn. cursor()
id = input('id: ')
nome = input ('nome: ')
idade = input('idade')

#executando a função SQL insert
cursor.execute ("insert into estudantes (id, nome, idade) values (?,  ?, ?)", (id, nome, idade,))

cursor.execute("SELECT * FROM estudantes")
registros = cursor.fetchall()

#uso do For para ver registros no python
for registro in registros:
    print(registro)

conn.commit()
cursor.close()
conn.close()

