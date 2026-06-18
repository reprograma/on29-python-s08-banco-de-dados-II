import csv
import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def exportar_csv():
  cursor.execute("SELECT titulo, autor, ano, preco FROM livros")
  dados = cursor.fetchall()
  with open('exportados.csv', 'w', newline='') as exportados_livros:
    escritor = csv.writer(exportados_livros)
    escritor.writerow(['titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(dados)
  conn.commit()
