#Crie um script que remova o registro de um estudante específico (por exemplo, remova "Charlie").

import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

conn.commit()
cursor.close()
conn.close()