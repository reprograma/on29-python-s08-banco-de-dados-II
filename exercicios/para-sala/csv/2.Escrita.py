import csv

novos_dados = [
       [6, 'Carlota', 'Financeiro'],
       [7, 'Joaquina', 'TI'],
       [8, 'Bianca', 'RH']
]

with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'departamento'])
    escritor.writerows(novos_dados)