import sqlite3

conn =sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("update estudantes set idade = ? where nome = ?", (23,'bob'))

conn.commit()
cursor.close()
conn.close()
