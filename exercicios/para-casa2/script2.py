"""2. **Importação de Dados de um CSV**
    - Crie um arquivo CSV chamado `livros.csv` com as colunas `titulo`, `autor`, `ano`, e `preco`.
    - Adicione pelo menos 5 registros no arquivo `livros.csv`.
    - Escreva um script Python que leia os dados de `livros.csv` e insira-os na tabela `livros`."""


import csv

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