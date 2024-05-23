import sqlite3
import csv

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

with open('livros.csv', 'r', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)
    for registro in leitor:
        cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)", (registro[0], 
                                                                                              registro[1], 
                                                                                              registro[2], 
                                                                                              registro[3]))

conn.commit()
cursor.close()
conn.close()