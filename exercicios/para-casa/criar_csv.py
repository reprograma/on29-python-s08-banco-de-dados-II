import csv

def criar_csv():
    books = [
        ['Violet Bent Backwards over the Grass','Lana Del Rey', 2020, 273.99],
        ['Mulheres que correm com os lobos','Clarissa Pinkola Estés', 1989, 69.99],
        ['O fato e a coisa', 'Torquato Neto', 2022, 49.99],
        ['Vidas Secas','Graciliano Ramos', 1938, 45.99],
        ['A Hora da Estrela', 'Clarice Lispector', 1977, 23.99]
    ]
    with open('livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(['titulo', 'autor', 'ano', 'preco'])
        escritor.writerows(books)
     
        
criar_csv()
