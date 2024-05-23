#4. **Atualização de Dados**:
#   - Escreva um script que atualize a idade de um estudante específico (por exemplo, mude a idade de "Bob" 
# para 23).
import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()
nome = input("nome: ")
idade = input("idade: ")
id = input("id: ")

cursor.execute("UPDATE estudantes SET idade = ? WHERE id = ?", (idade, nome, id))

for registro in registros:
    print(registro)

conn.commit()
cursor.close()
conn.close()