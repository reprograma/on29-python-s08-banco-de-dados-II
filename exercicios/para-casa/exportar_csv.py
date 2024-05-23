# Importa a biblioteca sqlite3
# Importa a biblioteca csv 
# Conecta ao banco de dados
# Cria um cursor
# Selecionar todos os registros da tabela 'livros'
# Pegar todos os registros
# Abrir um arquivo CSV para escrita
# Criar um escritor de CSV
# Escrever o cabeçalho no arquivo CSV
# Escrever todos os registros no arquivo CSV



import sqlite3   
import csv 

conn = sqlite3.connect('livraria.db')


cursor = conn.cursor()


cursor.execute('SELECT * FROM livros')

 
rows = cursor.fetchall()


with open('exportados_livros.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    
   
    writer.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    
    
    writer.writerows(rows)

# Fecha a conexão com o banco de dados
conn.close()

# Imprime uma mensagem indicando que os dados foram exportados com sucesso
print("Dados exportados com sucesso para o novo arquivo CSV!")
