# Importa a biblioteca sqlite3 
# Abrir conexão com banco de dados
# Criar um cursor
# Remover o livro 
# Comita as mudanças 
# Fechar a conexão 

import sqlite3  


conn = sqlite3.connect('livraria.db')


cursor = conn.cursor()


cursor.execute('''
    DELETE FROM livros
    WHERE id = ?
''', (3,))


conn.commit()


conn.close()


print("Desaquendou o livro!!!!")
