"""5. **Remoção de Dados**:
   - Crie um script que remova um estudante específico (por exemplo, remova "Charlie")."""


import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

estudantes = [
    ('Luis', 55)
]

cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)
cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Luis',))

conn.commit()
cursor.close()
conn.close()