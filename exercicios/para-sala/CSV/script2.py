"""9. **Importação de CSV para SQLite**:
   - Crie um script que leia um arquivo CSV chamado `clientes.csv` e insira os dados em uma tabela `clientes` no banco de dados SQLite `empresa.db`. A tabela deve ter as colunas `id`, `nome`, `email`.
"""

import sqlite3
import csv

conn = sqlite3.connect('empresa.db') # cria a conexão com o banco de dados
cursor = conn.cursor() # cria o cursor para andar dentro do db

# criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")
# 1. verifica se existe clientes.csv, 2. cria a ultima linha vazia e encoding formata como um arquivo csv (csvfile)
with open('clientes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile) # armazena tudo lido na variavel leitor
    next(leitor)  # Pular o cabeçalho para ler somente o conteúdo útil 
    for linha in leitor: # a partir disso, começa a percorrer cada linha
        
        # aqui ele vai inserir tudo que estiver nas linhas 1 e 2 (menos o cabeçalho) no banco de dados
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (linha[1], linha[2]))

conn.commit() # comenta as alterações 
cursor.close() # desliga o cursor
conn.close() # desliga a conexão