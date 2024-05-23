import sqlite3
from banco.sql import execute_sql

conn = sqlite3.Connection("livraria.db")
cursor = conn.cursor()
nome_tabela = "livros"
dados_create = ["id INTEGER PRIMARY KEY", "nome TEXT", "idade INTEGER"]

execute_sql.create_sql(cursor, nome_tabela, dados_create)