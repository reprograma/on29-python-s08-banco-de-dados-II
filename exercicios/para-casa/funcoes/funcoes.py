import sqlite3
import csv

def criar_banco_dados_tabela():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("""
   CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    ano INTEGER,
    preco REAL NOT NULL
   )
   """)

    conn.commit()
    cursor.close()
    conn.close()
    return print("Banco criado")


def importar_csv():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("""
   CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    ano INTEGER,
    preco REAL NOT NULL
   )
   """)

    with open('livros.csv', newline='', encoding='utf-8') as csvfile:
       leitor = csv.reader(csvfile)
       next(leitor)  # Pular o cabeçalho
       for linha in leitor:
           cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (linha[0], linha[1], linha[2], linha[3]))

    conn.commit()
    cursor.close()
    conn.close()

def exibir_dados():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    registros = cursor.fetchall()

    for registro in registros:
       print(registro)

    cursor.close()
    conn.close()

def atualizar_dados(id, valor):
   conn = sqlite3.connect('livraria.db')
   cursor = conn.cursor()

   cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (valor, id))

   conn.commit()
   cursor.close()
   conn.close()

def remover_dados(id):
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM livros WHERE id = ?", (id,))

    conn.commit()
    cursor.close()
    conn.close()

def exportar_csv():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    dados = cursor.fetchall()

    with open('exportados_livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
        escritor.writerows(dados)

    cursor.close()
    conn.close()
