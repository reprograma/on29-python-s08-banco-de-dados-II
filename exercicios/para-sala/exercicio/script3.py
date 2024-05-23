"""4. **Atualização de Dados**:
- Escreva um script que atualize a idade de um estudante específico (por exemplo, mude a idade de "Bob" para 23).
"""
import sqlite3

conn = sqlite3.connect('escola.db') # conecta com o banco de dados
cursor = conn.cursor() # cria o cursor que andará dentro do banco de dados

cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Edu')) # direciona o cursor para execução do comando SQL

conn.commit() # comenta a alteração 
cursor.close() # encerra a atividade do cursor
conn.close() # desconecta do banco de dados