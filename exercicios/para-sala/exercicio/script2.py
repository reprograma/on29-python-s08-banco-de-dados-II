# 3. **Consulta de Dados**

import sqlite3

conn = sqlite3.connect('escola.db') # conectar com o banco de dados
cursor = conn.cursor() # criar o cursor para mexer dentro do banco de dados

nome = input("digite um nome: ")
cursor.execute("SELECT nome FROM estudantes WHERE nome = ?", (nome,))

#cursor.execute("SELECT * FROM estudantes") # forçar o cursor a executar o comando "selecionar tudo"
registros = cursor.fetchall() # depois de pegar todas as informações, o comando fetchall guarda todas as informaçoes dentro de registros

for registro in registros: # passa linha a linha
    print(registro) # e printa tudo que ta dentro da variavel percorrido pelo comando for

cursor.close()
conn.close()