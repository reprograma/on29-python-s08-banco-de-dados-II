#5. **Remoção de Dados**:
#- Crie um script que remova um estudante específico (por exemplo, remova "Charlie").

import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

nome = 'Charlie'

cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

conn.commit()
cursor.close()
conn.close()