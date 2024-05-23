import sqlite3

#criar conexão
conn = sqlite3.connect('escola.db')
# criar cursor para uso do SQL
cursor = conn.cursor()

nome = input("Digite um nome: ")


#executar a função no SQL
cursor.execute("SELECT nome FROM estudantes WHERE nome = ? ", (nome,))
registros = cursor.fetchall()

#uso do For para ver registros no python
for registro in registros:
    print(registros)

#Fechar cursor
cursor.close()
#fechar conexão
conn.close()

