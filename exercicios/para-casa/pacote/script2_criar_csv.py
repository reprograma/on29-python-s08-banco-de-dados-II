import csv
import sqlite3

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

