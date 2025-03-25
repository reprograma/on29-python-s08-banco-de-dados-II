# Importar a biblioteca sqlite3
# Abrir conexão com banco de dados
# Criar um cursor
# Atualizar o preço 
# Comita as mudanças 
# Fechar a conexão com o banco de dados

import sqlite3  


conn = sqlite3.connect('livraria.db')


cursor = conn.cursor()


cursor.execute('''
    UPDATE livros
    SET preco = ?
    WHERE id = ?
''', (29.99, 1))


conn.commit()


conn.close()

# Imprime uma mensagem indicando que o livro foi atualizado
print("LACROU !!! Preço atualizado!")
