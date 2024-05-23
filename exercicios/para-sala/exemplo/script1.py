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

cursor.execute ("insert into usuarios (nome, idade) values ('joao', 43)")
cursor.execute ("insert into usuarios (nome, idade) values ('jessica', 23)")

cursor.execute ("select * from usuarios")
registros = cursor.fetchall()

for registro in registros:
    print(registros)

conn.commit()
conn.close()
