#2. Criar arquivo csv, inserir dados e registra-los no banco de dados.

import csv
import sqlite3

conn = sqlite3.connect("livraria.db")
cursor = conn.cursor()
#criar arquivo livros.csv
cursor.execute("SELECT id, titulo, autor, ano, preco FROM livros")
dados = cursor.fetchall()
#adicionar 5 registros
livros = [
    ('Pele Negra, Máscaras Brancas', 'Franz Fanon', 1952, 35.90),
    ('Admirável Mundo Novo', 'Aldous Huxley', 1932, 39.90),
    ('Memórias Póstumas de Brás Cubas', 'Machado de Assis', 1881, 10.90),
    ('Jogos Vorazes', 'Suzanne Collins', 2008, 25.90),
    ('Tudo sobre o Amor', 'Bell Hooks', 1999, 50.90)
]
#um script Python que leia os dados de `livros.csv'
with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'autor', 'ano', 'preco'])
    escritor.writerows(livros)

#insira-os na tabela `livros`.
cursor.executemany("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", livros,)

conn.commit()
cursor.close()
conn.close()