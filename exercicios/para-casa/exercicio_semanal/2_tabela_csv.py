import csv

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