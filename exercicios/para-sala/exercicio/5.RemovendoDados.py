import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Julia',))

cursor.execute("SELECT * FROM estudantes")
registros = cursor.fetchall()
for registro in registros:
    print(registro)

conn.commit()
cursor.close()
conn.close()