
import sqlite3

def delete(opt2,coon):
    
    coon = sqlite3.connect('livraria.db')
    cursor = coon.cursor()
    
    cursor.execute("DELETE FROM livros where id = ?" ,(opt2))


    coon.commit()
    
