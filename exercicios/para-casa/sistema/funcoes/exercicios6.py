
import csv 
import sqlite3

def exportar_arquivo(coon, colunas):
    
    conn = sqlite3.connect('livraria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    dados = cursor.fetchall()

    with open('exportados_livros.csv', 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(colunas)
        escritor.writerows(dados)

    print("Aquivo exportado")
