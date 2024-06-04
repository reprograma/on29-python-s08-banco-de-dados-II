
import sqlite3

def colsulta_csv(coon):
    
    coon = sqlite3.connect('livraria.db')
    cursor = coon.cursor()

    cursor.execute("select * from livros")
    registros = cursor.fetchall()

    for registro in registros:
        print(registro)
    
    coon.commit()
    
    

    return print(registro)
