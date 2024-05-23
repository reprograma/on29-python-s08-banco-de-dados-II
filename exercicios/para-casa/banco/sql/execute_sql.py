import sqlite3


def create_sql(cursor, nome_tabela, dados):
    colunas = " ,". join(dados)
    sql = f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({colunas})"
    resposta = cursor.execute(sql)
    return resposta

def insert_sql(cursor, nome_tabela, dados):
    resposta = cursor.executemany("INSERT INTO ? (titulo,autor,ano,preco) VALUES (?, ?, ?, ?)", (nome_tabela, dados))
    return resposta
    