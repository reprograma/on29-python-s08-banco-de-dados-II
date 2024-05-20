import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

id = input("Digite o ID do estudante que deseja atualizar: ")
novo_nome = input("Digite o novo nome: ")
nova_idade = int(input("Digite a nova idade: "))

cursor.execute("UPDATE estudantes SET nome = ?, idade = ? WHERE id = ?", (novo_nome, nova_idade, id))

cursor.execute("SELECT * FROM estudantes")
# 'cursor.fetchall()' - Percorre todos os registros resultantes da última instrução SQL
registros = cursor.fetchall()
for registro in registros:
    print(registro)

conn.commit()
cursor.close()
conn.close()

