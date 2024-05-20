# Exercício de casa
# Integração Completa de CSV com SQLite usando Python

# Importando as bibliotecas necessárias
import sqlite3
import csv
import os

# Criação do Banco de Dados e Tabela
conn = sqlite3.connect('livraria.db')
def criar_banco_e_tabela():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        ano INTEGER,
        preco REAL
    )
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados e tabela criados com sucesso.")

# Importação de Dados de um CSV
def importar_csv_para_tabela():
    if not os.path.exists('livros.csv'):
        print("Arquivo livros.csv não encontrado.")
        return
    
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()
    
    with open('livros.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('''
            INSERT INTO livros (titulo, autor, ano, preco)
            VALUES (?, ?, ?, ?)
            ''', (row['titulo'], row['autor'], row['ano'], row['preco']))
    
    conn.commit()
    conn.close()
    print("Dados importados com sucesso do CSV para a tabela.")

# Consulta e Exibição de Dados
def exibir_registros():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    rows = cursor.fetchall()
    conn.close()
    
    if rows:
        for row in rows:
            print(row)
    else:
        print("Nenhum registro encontrado.")

# Atualização de Dados
def atualizar_preco_livro(livro_id, novo_preco):
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE livros
    SET preco = ?
    WHERE id = ?
    ''', (novo_preco, livro_id))
    
    conn.commit()
    conn.close()
    print("Preço atualizado com sucesso.")

# Remoção de Dados
def remover_livro(livro_id):
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    DELETE FROM livros
    WHERE id = ?
    ''', (livro_id,))
    
    conn.commit()
    conn.close()
    print("Livro removido com sucesso.")

# Exportação de Dados para CSV
def exportar_tabela_para_csv():
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM livros')
    rows = cursor.fetchall()
    conn.close()
    
    with open('exportados_livros.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
        writer.writerows(rows)
    print("Dados exportados com sucesso para exportados_livros.csv.")

# Função menu, onde as funções criadas para a resolução do exercício serão chamadas

def menu():
    while True:
        print("+------------------------------------------------------------------+")
        print("+                       Livraria Reprograma                        +")
        print("+------------------------------------------------------------------+")
        print("+ 1. Criar banco de dados e tabela                                 +")
        print("+ 2. Importar dados do CSV para a tabela                           +")
        print("+ 3. Exibir todos os registros                                     +")
        print("+ 4. Atualizar preço de um livro                                   +")
        print("+ 5. Remover um livro                                              +")
        print("+ 6. Exportar dados da tabela para um CSV                          +")
        print("+ 0. Sair                                                          +")
        print("+------------------------------------------------------------------+")

        opt = input("+ Escolha uma opção: ")
        
        if opt == '1':
            criar_banco_e_tabela()

        elif opt == '2':
            importar_csv_para_tabela()

        elif opt == '3':
            exibir_registros()

        elif opt == '4':
            livro_id = int(input("+ Digite o ID do livro que deseja atualizar: "))
            novo_preco = float(input("+ Digite o novo preço: "))

            atualizar_preco_livro(livro_id, novo_preco)

        elif opt == '5':
            livro_id = int(input("+ Digite o ID do livro que deseja remover: "))

            remover_livro(livro_id)

        elif opt == '6':
            exportar_tabela_para_csv()

        elif opt == '0':
            print("Obrigad@, volte sempre!")
            break

        elif opt not in ["1", "2", "3", "4", "5", "6", "0"]:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()