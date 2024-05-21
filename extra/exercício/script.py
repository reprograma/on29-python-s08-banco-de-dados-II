import sqlite3

conn = sqlite3.connect("vendas.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL
); 
               """)

# cursor.executemany("INSERT INTO vendas (produto, quantidade, preco) VALUES (?, ?, ?)", [
#     ('Produto A', 10, 5.0),
#     ('Produto B', 5, 10.0),
#     ('Produto C', 2, 20.0),
#     ('Produto A', 3, 5.0),
#     ('Produto B', 7, 10.0)
# ])

conn.commit()

# cursor.execute("""
#                select produto, sum(quantidade) as total_quantidade 
#                from vendas 
#                group by produto
#                """)
# print(cursor.fetchall())

# cursor.execute("""
#                Select produto, AVG(preco) as preco_medio from vendas group by produto
#                """)
# print(cursor.fetchall())


# cursor.execute("SELECT produto, MAcX(preco) AS preco_maximo FROM vendas GROUP BY produto")
# print(cursor.fetchall())

# nome_produto = "Produto A"

# cursor.execute("INSERT INTO vendas (produto, quantidade, preco) VALUES (?, ?, ?)", 
#      (nome_produto, 14, 8.0))

# conn.commit()

cursor.execute("SELECT produto, MIN(preco) AS preco_minimo FROM vendas GROUP BY produto")
print(cursor.fetchall())
