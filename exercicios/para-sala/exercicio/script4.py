import sqlite3


conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

nome = 'Charlie'

cursor.execute("DELETE FROM estudantes WHERE nome = ?", (nome,))

conn.commit()
cursor.close()
conn.close()