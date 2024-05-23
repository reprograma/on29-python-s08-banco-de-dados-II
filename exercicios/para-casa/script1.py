import sqlite3
import csv

# 1. **Criação do Banco de Dados e Tabela**
def criar_db():
    conn = sqlite3.connect('livraria.db') # conexão 
    cursor = conn.cursor() # criar o cursor para usar dentro do sqlite

    # comandos SQL para criação da tabela
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER NOT NULL,
        preco REAL
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

criar_db()

#2. **Importação de Dados de um CSV**
def criar_csv():
    livros = [
        (1, '1984', 'George Orwell', 1949, 28.90),
        (2, 'Ninguém é de ninguém', 'Zibia Gasparetto', 2003, 43.00),
        (3, 'Um gato entre os pombos', 'Agatha Christie', 1959, 24.70),
        (4, 'Manual prático de como se perder a alma', 'Diedra Roiz', 2009, 0.00),
        (5, '[10] coisas que eu odeio em você', 'Diedra Roiz', 2006, 24.99),
        (6, 'Duas mulheres sozinhas e outros contos', 'Diedra Roiz', 2006, 2.99)          
    ]
        
    colunas = ['id', 'titulo', 'autor', 'ano', 'preco']  # Nome das colunas
    
    with open('./livros.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile, delimiter= ',')
        escritor.writerow(colunas)  # Escrever o cabeçalho
        escritor.writerows(livros)  # Escrever os dados

# Chamar a função para criar o arquivo CSV
criar_csv()

def importar_dadoscsv():
    conn = sqlite3.connect('livraria.db') # cria a conexão com o banco de dados
    cursor = conn.cursor() # cria o cursor para andar dentro do db

    # 1. verifica se existe clientes.csv, 2. cria a ultima linha vazia e encoding formata como um arquivo csv (csvfile)
    with open('./livros.csv', newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile) # armazena tudo lido na variavel leitor
        next(leitor)  # Pular o cabeçalho para ler somente o conteúdo útil 
        
        for linha in leitor: # a partir disso, começa a percorrer cada linha
            id, titulo, autor, ano, preco = linha
            # aqui ele vai inserir tudo que estiver nas linhas 1 e 2 (menos o cabeçalho) no banco de dados
            cursor.execute("INSERT INTO livros (id, titulo, autor, ano, preco) VALUES (?, ?, ?, ?, ?)", (id, titulo, autor, ano, preco))

    conn.commit() # comenta as alterações 
    cursor.close() # desliga o cursor
    conn.close() # desliga a conexãoconn = sqlite3.connect('empresa.db') # cria a conexão com o banco de dados
    cursor = conn.cursor() # cria o cursor para andar dentro do db
importar_dadoscsv()


# 3. **Consulta e Exibição de Dados**
def exibir_db(livros):
    return livros

# 4. **Atualização de Dados**
def atualizar_dados():
    return atualizar_dados

# 5. **Remoção de Dados**
def remover_dados():
    return remover_dados

# 6. **Exportação de Dados para CSV**
def exportar_dados(livros_exportados):
    return livros_exportados




