
import csv
import sqlite3

def criar_csv(tabela,linha_csv,col_csv,coon):
   
    cursor = coon.cursor()


    with open(f'{tabela}', 'w', newline='', encoding='utf-8') as csvfile:
       escritor = csv.writer(csvfile)
       escritor.writerow(col_csv)
       escritor.writerows(linha_csv)


    with open(f'{tabela}', newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        next(leitor)
        for linha in leitor:
            placeholders = ', '.join('?' * len(col_csv))
            sql = f"INSERT INTO livros ({', '.join(col_csv)}) VALUES ({placeholders})"
            
            try:
                cursor.execute(sql, linha)
            except sqlite3.OperationalError as e:
                print(f"Erro ao inserir dados: {e}")

    coon.commit()

    
    
    



    
       
    



