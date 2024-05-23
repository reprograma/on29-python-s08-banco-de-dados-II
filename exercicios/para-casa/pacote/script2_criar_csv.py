import csv
import sqlite3

def criar_csv():
  dados = [
      ['titulo', 'autor', 'ano', 'preco'],
      ['Harry Potter e a Pedra Filosofal', 'Emma Watson', 1997, 32.43], 
      ['Harry Potter e a Câmara Secreta', 'Emma Watson', 1998, 35.20], 
      ['Harry Potter e o Prisioneiro de Askaban', 'Emma Watson', 1999, 23.90],
      ['Harry Potter e o Cálice de Fogo', 'Emma Watson', 2000, 29.90],
      ['Harry Potter e a Ordem da Fênix', 'Emma Watson', 2003, 42.50]
  ]

  with open('livros.csv', 'w', newline='') as livros_csv:
      escritor = csv.writer(livros_csv)
      escritor.writerows(dados)

