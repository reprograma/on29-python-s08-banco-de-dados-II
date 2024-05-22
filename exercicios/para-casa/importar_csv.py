import csv


colunas = ['id', 'titulo', 'autor', 'ano','preco']
livros = [
        (1,'Galinha Pintadinha','Zeca tatu',2020, 10.00),
        (2,'O Judas perdeu as botas','Xuxu beleza',2001, 5.00),
        (3,'Ceu azul','Rosalia',2000, 15.00),
        (4,'A terra do nunca','Oscalina',2023, 12.00),
        (5,'Tempo perdido','Renato Russo',1990, 18.00)
]


with open('./livros.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile, delimiter= ',')
    escritor.writerow(colunas)  # Escrever o cabeçalho
    escritor.writerows(livros)  # Escrever os dados
