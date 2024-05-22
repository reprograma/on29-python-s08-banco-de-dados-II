import csv
import sqlite3

conn = sqlite3.connect("livraria.db")
cursor = conn.cursor()

def criar_tabela_banco():
   cursor.execute("""
      CREATE TABLE IF NOT EXISTS livros (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      titulo TEXT NOT NULL,
      autor TEXT NOT NULL,
      ano INTEGER NOT NULL,
      preco REAL NOT NULL
      )
      """)

   conn.commit()
def criar_csv():
  dados = [
      ['titulo', 'autor', 'ano', 'preco'],
      ['Dom Casmurro', 'Machado de Assis', 1899, 32.43], 
      ['Orgulho e preconceito', 'Jane Austen', 1813, 35.20], 
      ['O Diário de Anne Frank', 'Anne Frank', 1947, 23.90],
      ['Percy Jackson', 'Rick Riordan', 2005, 29.90],
      ['Fahrenheit 451', 'Ray Bradbury', 1953, 42.50]
  ]

  with open('livros.csv', 'w', newline='') as livros_csv:
      escritor = csv.writer(livros_csv)
      escritor.writerows(dados)
def importar_csv():
  with open('livros.csv', 'r') as livros_csv:
    leitor = csv.reader(livros_csv)
    next(leitor)
    for linha in livros_csv:
      cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", linha.split(','))

  conn.commit()
def consultar_livros():
  cursor.execute("SELECT * FROM livros")
  resultados = cursor.fetchall()
  conn.commit()
  for linha in resultados:
    print(linha)
def atualizar_livro():
  cursor.execute("UPDATE livros SET preco = ? WHERE titulo = ?", (32.50, 'Dom Casmurro'))
  conn.commit()
def remover_livro():
  cursor.execute("DELETE FROM livros WHERE id = ?", (2,))
  conn.commit()
def exportar_csv():
  cursor.execute("SELECT titulo, autor, ano, preco FROM livros")
  dados = cursor.fetchall()
  with open('exportados.csv', 'w', newline='') as exportados_livros:
    escritor = csv.writer(exportados_livros)
    escritor.writerow(['titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(dados)

  cursor.close()
  conn.close()

criar_tabela_banco()
criar_csv()
importar_csv()
consultar_livros()
atualizar_livro()
remover_livro()
exportar_csv()

print("Programa concluído com sucesso!")

