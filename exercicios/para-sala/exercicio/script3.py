import sqlite3

# Criar conexão
conn = sqlite3.connect('escola.db')
# cursor para uso do SQL
cursor = conn.cursor()

#Criar tabela de insersão de dados
estudantes = [
       ('Alice', 21),
       ('Bob', 22),
       ('Charlie', 23)
   ]

#inserir varios dados de uma vez
cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

#fechar conexão
conn.commit()
#fechar cursor
cursor.close()
conn.close()