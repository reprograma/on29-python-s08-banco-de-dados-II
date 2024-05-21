#3. **Consulta e Exibição de Dados**
#    - Escreva um script Python que selecione e exiba todos os registros da tabela `livros`.

import sqlite3

conn = sqlite3.connect("livraria.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
registros = cursor.fetchall()

for registro in registros:
    print(registro)
    
cursor.close()
conn.close()