

import sqlite3

def conectar_db(banco):


    coon = sqlite3.connect(banco)
    return coon



def tabelas(coon, nome_tabela, *args):
    cursor = coon.cursor()

    col = ', '.join(args)

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {nome_tabela} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        {col}
    )
    """)

    coon.commit()
    
    