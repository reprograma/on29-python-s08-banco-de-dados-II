import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("UPDATE estudantes SET idade = ? WHERE id = ?", (18, 2))

cursor.execute("SELECT * FROM estudantes")
registros = cursor.fetchall()
for registro in registros:
    print(registro)

conn.commit()
cursor.close()
conn.close()

