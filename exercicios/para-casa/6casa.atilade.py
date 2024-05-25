import csv
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Seleciona todos os registros da tabela 'livros'
cursor.execute("SELECT * FROM livros")
livros = cursor.fetchall()

# Define o nome das colunas
colunas = [desc[0] for desc in cursor.description]

# Criação do arquivo CSV
with open('exportados_livros.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escreve o cabeçalho
    escritor_csv.writerow(colunas)
    
    # Escreve os dados
    escritor_csv.writerows(livros)

# Fecha a conexão
cursor.close()
conn.close()

print("Dados exportados para 'exportados_livros.csv' com sucesso.")
