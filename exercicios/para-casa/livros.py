import csv
import sqlite3

def banco_e_tabela():
    conn = sqlite3.connect("livraria.db")
    cursor = conn.cursor()
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
    cursor.close()
    conn.close()


def livros_csv():
    conn = sqlite3.connect("livraria.db")
    cursor = conn.cursor()

    with open('livros.csv', 'r' , newline='', encoding='utf-8') as csvfile:
        livros = csv.DictReader(csvfile)
        for row in livros:
            cursor.execute('''
                       INSERT INTO livros (titulo, autor, ano, preco)
                           VALUES (?, ?, ?, ?)
                       ''', (row['titulo'], row['autor'], int(row['ano']), float(row['preco'])))
    conn.commit()
    cursor.close()
    conn.close()


def consultar_livros():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    dados = cursor.fetchall()
    print("Registros da tabela livros:")
    for row in dados:
        print(row)
    conn.commit()
    cursor.close()
    conn.close()

banco_e_tabela()
livros_csv()
consultar_livros()

def atualizar_preco():

    try:
        conn = sqlite3.connect('livraria.db')
        cursor = conn.cursor()

        id = int(input("Qual o ID do livro? "))
        novo_preco = float(input("Digite o novo preço do livro: "))

        cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, id))
        conn.commit()

        if cursor.rowcount == 0:
            print(f"Desculpe, nenhum livro foi encontrado com o ID {id}. Digite um ID válido!")
        else:
            print(f"O preco do livro foi atualizado para {novo_preco}!")

    except ValueError:
        print(f"ID ou preco inválido. Verifique os números e tente novamente.")
    
    finally:
        if cursor is not None:
            cursor.close()
        if cursor is not None:
            conn.close()

atualizar_preco()

def remover_livro():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("DELETE from livros WHERE id = ?", ('Eu sou Malala'))

    conn.commit()
    cursor.close()
    conn.close()

remover_livro()

