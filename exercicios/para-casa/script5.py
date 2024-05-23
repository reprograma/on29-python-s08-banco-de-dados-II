import sqlite3

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
registros = cursor.fetchall()

with open('exportados_livros.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = arquivo_csv.writer(arquivo_csv)
    
    escritor.writerow(['id', 'titulo', 'autor', 'ano', 'preco'])
    
    for registro in registros:
        escritor.writerow(registro)


conn.close()