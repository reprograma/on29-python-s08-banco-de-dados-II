import sqlite3

conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    )
    """)

# cursor.executemany("INSERT INTO vendas (produto, quantidade, preco) VALUES (?, ?, ?)", [
#     ('Produto A', 10, 5.0),
#     ('Produto B', 5, 10.0),
#     ('Produto C', 2, 20.0),
#     ('Produto A', 3, 5.0),
#     ('Produto B', 7, 10.0)
# ])

conn.commit()

# -------------------------------------------------------------------------------------------------

# Somando a quantidade de produtos vendidos de acordo com cada entrada de compra
# cursor.execute("SELECT produto, SUM(quantidade) AS total_quantidade FROM vendas GROUP BY produto")
# print(cursor.fetchall())

# -------------------------------------------------------------------------------------------------

# Calculando a média de preços de acordo com cada entrada de compra
# cursor.execute("SELECT produto, AVG(preco) AS preco_medio FROM vendas GROUP BY produto")
# print(cursor.fetchall())

# -------------------------------------------------------------------------------------------------

# Contando a quantidade de registros (nesse caso, vendas)
# cursor.execute("SELECT COUNT(*) AS total_vendas FROM vendas")
# print(cursor.fetchall())

# -------------------------------------------------------------------------------------------------

# Conferindo o maior preço já registrado em alguma venda
# cursor.execute("SELECT MAX(preco) AS preco_maximo FROM vendas")
# print(cursor.fetchall())

# -------------------------------------------------------------------------------------------------

# Conferindo o maior preço pelo qual cada produto foi vendido
# cursor.execute("SELECT produto, MAX(preco) AS preco_maximo FROM vendas GROUP BY produto")
# print(cursor.fetchall())

# -------------------------------------------------------------------------------------------------

#Conferindo o menor preço ja registrado em alguma venda
# cursor.execute("SELECT MIN(preco) AS preco_minimo FROM vendas")
# print(cursor.fetchall())

# -------------------------------------------------------------------------------------------------

#Conferindo o menor preço pelo qual cada produto foi vendido
# cursor.execute("SELECT produto, MIN(preco) AS preco_minimo FROM vendas GROUP BY produto")
# print(cursor.fetchall())