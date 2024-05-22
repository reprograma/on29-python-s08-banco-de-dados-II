import csv
import sqlite3

def menu():
    while True:
        print(' ')
        print('---- LIVRARIA PONEINAC ----')
        print('Criar um Database e uma tabela - 1')
        print('Criar um arquivo CSV e inserir no Database os 5 últimos livros lidos - 2')
        print('Consultar os registros do Database - 3')
        print('Atualizar o preço de um registro do Database - 4')
        print('Remover um registro do Database - 5')
        print('Exportar registros do Database para arquivo CSV - 6')
        print('Sair - 0')

        opt_cliente = input('Digite a opção desejada: ')
        if opt_cliente == '1':
            criar_db()
        elif opt_cliente == '2':
            csv_import()
        elif opt_cliente == '3':
            consulta_db()
        elif opt_cliente == '4':
            update_db()
        elif opt_cliente == '5':
            delete_db()
        elif opt_cliente == '6':
            export_db()
        elif opt_cliente == '0':
            print('Obrigada por usar o programa.')
            break
        else:
            print('Essa opção não é válida.')

def criar_db():
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
    print("--- Seu Database 'livraria.db' e sua tabela 'livros' foi criada com sucesso. ---")

def csv_import():
    colunas = ['id', 'titulo', 'autor', 'ano', 'texto']
    livros = [
        (1, 'Cartas para minha avó', 'Djamila Ribeiro', 2021, 36.78),
        (2, 'Aurora', 'Marcela Ceribelli', 2022, 37.42),
        (3, 'O peso do pássaro morto', 'Aline Bei', 2017, 51.80),
        (4, 'Torto arado', 'Itamar Vieira Junior', 2019, 52.43),
        (5, 'Primavera silenciosa', 'Rachel Carson', 1962, 50.99)
    ]

    with open('./livros.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile, delimiter= ',')
        escritor.writerow(colunas)
        escritor.writerows(livros)

    conn = sqlite3.connect("livraria.db")
    cursor = conn.cursor()
    print('--- Seus registros foram incluídos no arquivo .csv com sucesso. ---')

    with open ('livros.csv', newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            print("--- Os livros da sua lista 'livros.csv' são os seguintes: ", linha, ". ---")

    with open ('livros.csv', newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        next(leitor)
        for linha in leitor:
            cursor.execute('INSERT INTO livros (id, titulo, autor, ano, preco) VALUES (?, ?, ?, ?, ?)', (linha [0], linha[1], linha[2], linha [3], linha[4]))

    conn.commit()
    cursor.close()
    conn.close()
    print('--- Seus registros foram inseridos no Database com sucesso. ---')

def consulta_db():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM livros')
    registros = cursor.fetchall()
    for registro in registros:
        print("--- Registros da tabela 'livros': ", registro, ". ---")

def update_db():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()
    opt_id = input('Digite o id do livro: ')
    while (opt_id < '1') or (opt_id > '5'):
        print('--- Essa é uma opção inválida. Digite novamente. ---')
        opt_id = input('Digite o id do livro: ')
     
    opt_preco = float(input('Digite o preço atualizado - exemplo: 61.99: '))

    cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (opt_preco, opt_id))

    conn.commit()
    cursor.close()
    conn.close()
    print('--- O preço do seu registro foi atualizado com sucesso. ---')


def delete_db():
    conn = sqlite3.connect("livraria.db")
    cursor = conn.cursor()
    opt_id = input('Digite o id do livro que você quer remover da lista: ')
    while (opt_id < '1') or (opt_id > '5'):
        print('--- Essa é uma opção inválida. Digite novamente. ---')
        opt_id = input('Digite o id do livro que você quer remover da lista: ')

    cursor.execute("DELETE FROM livros WHERE id = ?", (opt_id,))

    conn.commit()
    cursor.close()
    conn.close()
    print('--- O registro escolhido foi excluído com sucesso. ---')


def export_db():
    conn = sqlite3.connect("livraria.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    with open ('livros_exportados.csv', 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
        escritor.writerows(livros)

    cursor.close()
    conn.close()
    print("--- Os registros do Database foram exportados para o arquivo 'livros_exportados.csv' com sucesso. ---")

menu()