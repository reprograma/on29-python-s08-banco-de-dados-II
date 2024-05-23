"""3. **Consulta e Exibição de Dados**
    - Escreva um script Python que selecione e exiba todos os registros da tabela `livros`."""

import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor() # criar o cursor para usar dentro do sqlite

cursor.execute("SELECT * FROM livros")
livros = cursor.fetchall()

for livro in livros:
    print(livro)

conn.commit()
cursor.close()
conn.close()