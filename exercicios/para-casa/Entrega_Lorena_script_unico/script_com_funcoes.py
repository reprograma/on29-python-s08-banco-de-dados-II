import sqlite3
import csv

def criar_banco_e_tabela():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            ano INTEGER,
            preco REAL
        )      
    """)

    conn.commit()
    cursor.close()
    conn.close()
    
    print("Banco de dados e tabela criados com sucesso.")
    
def importar_csv():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    with open('./livros.csv', newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        next(leitor)
        for linha in leitor:
            cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (linha[0], linha[1], linha[2], linha[3]))
            
    conn.commit()
    cursor.close()
    conn.close()
    print("Arquivo CSV importado com sucesso.")
    
def consultar_livros():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    livros_completo = cursor.fetchall()

    for livro in livros_completo:
        print(livro)

    cursor.close()
    conn.close()
    
def atualizar_livro(id_livro, novo_preco):
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, id_livro))

    conn.commit()
    cursor.close()
    conn.close()
    print("O preço do livro foi alterado com sucesso.")

def remover_livro(id_livro):
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro))

    conn.commit()
    cursor.close()
    conn.close()
    print("O livro foi removido com sucesso.")
    
def exportar_csv():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    livros_completo = cursor.fetchall()

    with open ('exportados_livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
        escritor.writerows(livros_completo)
        
    cursor.close()
    conn.close()
    print("Tabela exportada para o arquivo CSV com sucesso.")


def menu():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    while True:
        print("______________________________________________")
        print("\n  ========== LIVRARIA BOA LEITURA ==========")
        print("\n  Escolha a opção desejada do menu a seguir:")
        print("______________________________________________")
        
        print("\n1 - Criar uma tabela chamada 'livros 'dentro de um banco de dados com as informações de id, título, autor, ano e preço do livro.")
        print("2 - Importar os dados do arquivo CSV 'livros.csv' existente para a tabela 'livros'.")
        print("3 - Consultar os livros existentes na tabela 'livros'.")
        print("4 - Atualizar o preço de um determinado livro da tabela 'livros' através do seu id.")
        print("5 - Remover todas as informações de um livro da tabela 'livros' através do seu id.")
        print("6 - Exportar os dados da tabela 'livros' para um novo arquivo CSV.")
        print("0 - Sair do menu.")
        
        opcao = input("\nDigite aqui a opção desejada: ")
        
        if opcao == "1":
            criar_banco_e_tabela()

        elif opcao == "2":
            importar_csv()             
            
        elif opcao == "3":
            consultar_livros()
            
        elif opcao == "4":
            id_livro = input("Insira o id do livro que deseja atualizar o preço: ")
            novo_preco = input("Insira o novo preço: ")
            atualizar_livro(id_livro, novo_preco)
                        
        elif opcao == "5":
            id_livro = input("Insira o id do livro que deseja remover: ")
            remover_livro(id_livro)
                    
        elif opcao == "6":
            exportar_csv()
        
        elif opcao == "0":
            print("\nMenu encerrado.\n")
            break
        
        else:
            print("\nInsira uma opção válida.\n")
            continue
        
menu()