import sqlite3

conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )      
""")

# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('João', 25)")
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Maria', 20)")
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Chico', 40)")
# cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Buarque', 21)")

cursor.execute("SELECT * FROM usuarios")
registros = cursor.fetchall()
for registro in registros:
    print(registro)
               
conn.commit()
conn.close()