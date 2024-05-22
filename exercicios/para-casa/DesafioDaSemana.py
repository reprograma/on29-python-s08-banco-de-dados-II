import sqlite3
import csv



# **Criação do Banco de Dados e Tabela**
def criar_banco_tabela():
    
    conn = sqlite3.connect('Livraria.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano TEXT NOT NULL, 
            preco REAL
            )"""
    )
    
    conn.commit()
    conn.close()
    
# **Importação de Dados de um CSV**
def ler_csv():
    
    conn = sqlite3.connect('Livraria.db')
    cursor = conn.cursor()
    with open('livros.csv', newline='', encoding='UTF-8') as csv_file:
        leitor = csv.reader(csv_file)
        # Pula a primeira linha 
        next(leitor)
        for linha in leitor:
            cursor.execute('''
                INSERT INTO livros (titulo, autor, ano, preco)
                VALUES (?, ?, ?, ?)
                ''', (linha[0], linha[1], linha[2], linha[3]))
    
    conn.commit()
    conn.close()


# **Consulta e Exibição de Dados**

def Consultar_Visualizar():
    conn = sqlite3.connect('Livraria.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    for livro in livros:
        print(livro)
        
    conn.close()
    
# **Atualização de Dados**
    
def Atualizar_Preco():

    conn = sqlite3.connect('Livraria.db')
    cursor = conn.cursor()
    id_livro = int(input("Digite o id do livro a ter o preço modificado: "))
    novo_preco = float(input("Digite o novo valor para o livro: "))

    cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, id_livro))

    cursor.execute("SELECT * FROM livros")
    # 'cursor.fetchall()' - Percorre todos os registros resultantes da última instrução SQL
    livros = cursor.fetchall()
    for livro in livros:
        print(livros)

    conn.commit()
    conn.close()
    
# **Remoção de Dados**
    
def Remover_livros():
    conn = sqlite3.connect('Livraria.db')
    cursor = conn.cursor()
    id_livro = int(input("Digite o id do livro a ser removido: "))
    
    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))

    cursor.execute("SELECT * FROM livros")
    # 'cursor.fetchall()' - Percorre todos os registros resultantes da última instrução SQL
    livros = cursor.fetchall()
    for livro in livros:
        print(livro)
        
    conn.commit()
    conn.close()
    
# **Exportação de Dados para CSV**

def exportar_para_csv():
    conn = sqlite3.connect('Livraria.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    conn.close()
    
    with open('exportados_livros.csv', 'w', newline='', encoding='UTF-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])  
            for livro in livros:
                writer.writerows([str(valor) for valor in livro[1:]]) 

    print("Dados exportados.")
    

# Executando todas as etapas

def main():
    criar_banco_tabela()
    ler_csv()
    
    print("\nOs livros disponíveis são:")
    Consultar_Visualizar()
    
    Atualizar_Preco()
    Remover_livros()
    
    exportar_para_csv()
    print('\n***************************')
    print("\nDados exportados para arquivo csv.")
    
if __name__ == "__main__":
    main()
    

