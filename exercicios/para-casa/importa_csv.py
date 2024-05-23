# Importa a biblioteca sqlite3
# Importa a biblioteca csv
# Conecta ao banco de dados
# Cria um cursor
# Abre o arquivo CSV para leitura
# Cria um leitor de CSV
# Pula o cabeçalho do arquivo CSV
# Para cada linha no leitor de CSV
# Inserir os dados na tabela 'livros'
# Commita as mudanças 
# Fecha a conexão 

import sqlite3  
import csv   


conn = sqlite3.connect('livraria.db')


cursor = conn.cursor()


with open('livros.csv', 'r') as file:
   
    reader = csv.reader(file)
    
   
    next(reader)
    
   
    for row in reader:
        
        cursor.execute('''
            INSERT INTO livros (titulo, autor, ano, preco)
            VALUES (?, ?, ?, ?)
        ''', row)


conn.commit()

conn.close()


print("Pronto mona, tudo inserido!")
