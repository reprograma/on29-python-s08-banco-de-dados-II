import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def consultar_livros():
  cursor.execute("SELECT * FROM livros")
  resultados = cursor.fetchall()
  for linha in resultados:
    print(linha)
  conn.commit()