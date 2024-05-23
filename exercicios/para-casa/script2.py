import csv

# Dados dos 15 melhores livros brasileiros com preços estimados
livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "preco": 25.90},
    {"titulo": "Grande Sertão: Veredas", "autor": "João Guimarães Rosa", "ano": 1956, "preco": 42.00},
    {"titulo": "O Guarani", "autor": "José de Alencar", "ano": 1857, "preco": 19.90},
    {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "ano": 1881, "preco": 29.90},
    {"titulo": "Capitães da Areia", "autor": "Jorge Amado", "ano": 1937, "preco": 34.90},
    {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977, "preco": 22.50},
    {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890, "preco": 27.90},
    {"titulo": "Vidas Secas", "autor": "Graciliano Ramos", "ano": 1938, "preco": 28.50},
    {"titulo": "Iracema", "autor": "José de Alencar", "ano": 1865, "preco": 18.00},
    {"titulo": "O Auto da Compadecida", "autor": "Ariano Suassuna", "ano": 1955, "preco": 23.00},
    {"titulo": "Senhora", "autor": "José de Alencar", "ano": 1875, "preco": 21.50},
    {"titulo": "Macunaíma", "autor": "Mário de Andrade", "ano": 1928, "preco": 30.00},
    {"titulo": "A Moreninha", "autor": "Joaquim Manuel de Macedo", "ano": 1844, "preco": 20.00},
    {"titulo": "Quarup", "autor": "Antonio Callado", "ano": 1967, "preco": 35.00},
    {"titulo": "Lucíola", "autor": "José de Alencar", "ano": 1862, "preco": 24.50}
]

# Criar o arquivo CSV
with open('livros.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["titulo", "autor", "ano", "preco"])
    writer.writeheader()
    writer.writerows(livros)