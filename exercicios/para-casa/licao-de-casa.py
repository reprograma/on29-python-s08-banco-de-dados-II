import sqlite3
import csv

def menu():
    while True:
        print("Criar banco de dados - 1")
        print("Importar .CSV - 2")
        print("Consultar livros - 3")
        print("Atualizar livros - 4")
        print("Remover livro - 5")
        print("Exportar .csv - 6")
        print("Sair - 0")
        
        opcao = input("Digite a opção desejada:")
        lista = ['1', '2', '3', '4', '5', '6', '0']
        if opcao not in lista:
            print("Digite uma opção válida")
            continue
            
        
        if opcao == "1":
            criar_db()
        elif opcao == "2":
            importar_csv()
        elif opcao == "3":
            consultar_dados()
        elif opcao == "4":
            atualizar_dados()
        elif opcao == "5":
            remocao_dados()
        elif opcao == "6":
            exportar_dados()
        elif opcao == "0":
            break
        
def criar_db():
    conn = sqlite3.connect("livraria.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS livros(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               autor TEXT NOT NULL,
               ano INTEGER NOT NULL,
               preco REAL);
""")

    livros =[
    ('Atonement', 'Ian McEwan', 2001, 25.99),
    ('Do Androids Dream of Electric Sheep?', 'Philip K. Dick', 1968, 19.99),
    ('Fahrenheit 451', 'Ray Bradbury', 1953, 29.99),
    ('Into The Wild', 'Jon Krakauer', 1996, 15.99),
    ('On The Road', 'Jack Kerouac', 1957, 22.99)
    #('Mulheres que correm com os lobos', 'Clarissa Pinkola Estés', 1989, 66.99)
    ]
    cursor.executemany("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", livros)
    conn.commit()
    cursor.close()
    conn.close()


def importar_csv():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()
    
    with open('livros.csv', newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        next(leitor)
        for linha in leitor:
            cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (linha[0], linha[1], linha[2], linha[3]))
            cursor.execute("SELECT * FROM livros")
    conn.commit()
    cursor.close()
    conn.close()


def consultar_dados():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()
#tabela = livros
#DB = livraria
    cursor.execute("SELECT * FROM livros")
    registros = cursor.fetchall()

    for registro in registros:
        print(registro)

    cursor.close()
    conn.close()

def atualizar_dados():
    id = int(input("Informe a id do livro:"))
    novo_preco = float(input("Insira o novo preço do livro:"))
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE livros SET id = ? WHERE preco = ?", (id, novo_preco))

    conn.commit()
    cursor.close()
    conn.close()

def remocao_dados():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM livros WHERE id = ?", (id,))

    conn.commit()
    cursor.close()
    conn.close()

def exportar_dados():
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    dados = cursor.fetchall()

    with open('exportados_clientes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(['id', 'titulo','autor', 'ano', 'preco'])
        escritor.writerows(dados)

    cursor.close()
    conn.close()

menu()