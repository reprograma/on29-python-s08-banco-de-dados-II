import sqlite3
import csv


def criar_banco():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXTE NOT NULL,
        ano INTEGER NOT NULL,
        preco REAL NOT NULL        
        )
        """)

    conn.commit()
    cursor.close()
    conn.close()
    return print("Criação do bando de dados realizada!")


def import_csv():
    livros = [
        [1, 'A elite do atraso', 'Jessé Souza', 2017, 30.50],
        [2, 'Sexo no cativeiro', 'Esther Perel', 2018, 52.20],
        [3, 'A vida não é útil', 'Ailton Krenak', 2017, 21.22],
        [4, 'A coragem de ser imperfeito', 'Brené Brown', 2012, 26.79],
        [5, 'Inteligencia social', 'Daniel Goleman', 2019, 53.10]
    ]

    with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
        escritor.writerows(livros)

    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    with open('livros.csv', newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        next(leitor)
        for linha in leitor:
            cursor.execute("INSERT INTO livros (id, titulo, autor, ano, preco) VALUES (?, ?, ?, ?, ?)",
                           (linha[0], linha[1], linha[2], linha[3], linha[4]))

    conn.commit()
    cursor.close()
    conn.close()
    return print("Importação para arquivo CSV realizada com sucesso.")


def consulta_livros():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    registros = cursor.fetchall()

    for registros in registros:
        print(registros)

    cursor.close()
    conn.close()
    return print("Consulta e exbição da biblioteca: ")


def atualizar_livro():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE livros SET preco = 29.99 WHERE id = 1")

    conn.commit()
    cursor.close()
    conn.close()
    return print("Dados atualizados.")


def remocao_livro():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM livros WHERE id =3")

    conn.commit()
    cursor.close()
    conn.close()
    return print("Item excluido.")


def exportar_csv():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    dados = cursor.fetchall()

    with open('exportados_livros.csv', 'w', newline='', encoding='utf-8') as csvflie:
        escritor = csv.writer(csvflie)
        escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
        escritor.writerows(dados)

    cursor.close()
    conn.close()
    return print("Dados exportado para arquivo CSV.")
