import sqlite3

def atualizar(coon,opt2,opt3):

    coon = sqlite3.connect('livraria.db')
    cursor = coon.cursor()

    id = opt2
    preco = opt3
    cursor.execute("update livros set id = ? where preco =?", (id,preco))

    coon.commit()
    

