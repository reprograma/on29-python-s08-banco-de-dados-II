import csv
import sqlite3

from pacote import script1_criar_banco, script2_criar_csv, script2_importar_csv, script3_consultar_livros, script4_atualizar_livro, script5_remover_livro, script6_exportar_csv

funcao1 = script1_criar_banco.criar_banco()
funcao2 = script2_criar_csv.criar_csv()
funcao2_2 = script2_importar_csv.importar_csv()
funcao3 = script3_consultar_livros.consultar_livros()
funcao4 = script4_atualizar_livro.atualizar_livro()
funcao5 = script5_remover_livro.remover_livro()
funcao6 = script6_exportar_csv.exportar_csv()

print("Programa concluído com sucesso")