import csv
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

# Dados para o CSV
dados = [
    ['titulo', 'autor', 'ano', 'preco'],
    ['Porque Gritamos', 'Elizama Santos', 2023, 35.0],
    ['Escritos de uma vida', 'Sueli Carneiro', 2018, 50.0],
    ['Mitologia dos Orixas', 'Reginaldo Prandi', 2001, 80.0],
    ['Olhos Dagua', 'Conceição Evaristo', 2016, 5.0],
    ['Carta a minha filha', 'Maya Angelou', 2029, 65.0]
]

# Criação do arquivo CSV
with open('livros.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows(dados)

# Leitura e inserção de dados do CSV
with open('livros.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", linha)


# Confirma as mudanças e fecha a conexão
conn.commit()
cursor.close()
conn.close()