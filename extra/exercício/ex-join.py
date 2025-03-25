import sqlite3
conn = sqlite3.Connection("empresa.db")
cursor = conn.cursor()

cursor.execute("""
SELECT clientes.nome, pedidos.produto, pedidos.quantidade
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;
""")
print(cursor.fetchall())