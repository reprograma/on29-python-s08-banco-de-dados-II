# Importando o módulo 'sqlite3', para trabalhar com BD SQLite em Python.
import sqlite3

# Criando uma variável para conexão do python ao BD SQLite
conn = sqlite3.connect('escola.db')

# Criando o cursor (variável)
# O método 'cursor' (conn.cursor) permite executar comandos SQL e recuperar resultados de consultas
cursor = conn.cursor()

# Execução dos comandos SQL
# 'cursor.execute() - Executa a instrução SQL;
cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )              
""")

# Salvando as alterações realizadas
conn.commit()

# Fecha o cursor
cursor.close()

# Fechando a conexão com o Banco de dados
conn.close()