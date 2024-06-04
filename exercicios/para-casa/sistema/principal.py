

from funcoes import chamadas, exercicios1, entradas_usuario, exercicios2, exercicios3, exercicios4, exercicios5, exercicios6

chamadas.primeira_chamada()
db = entradas_usuario.nome_db()
coon = exercicios1.conectar_db(db)
tabela = entradas_usuario.nome_tabela()
col = entradas_usuario.colunas()
chamadas.segunda_chamada()
exercicios1.tabelas(coon, tabela,col)
colunas_csv = entradas_usuario.col_csv()
linhas_csv = entradas_usuario.valores_csv(colunas_csv)
aquivo_csv = exercicios2.criar_csv(tabela,linhas_csv,colunas_csv,coon)

controle = True 

opcoes = entradas_usuario.opcoes()
while controle:
    if opcoes == 1:
        consulta = exercicios3.colsulta_csv(coon)
    elif opcoes == 2:
        opt_id, opt_preco = entradas_usuario.atualizar_dados()
        atualizar = exercicios4.atualizar(coon,opt_id,opt_preco)
    elif opcoes == 3:
        opt_remover = entradas_usuario.remover()
        remover = exercicios5.delete(coon,opt_remover)
    elif opcoes == 4:
        controle = False
        print("Você escolheu a opção sair!")
    else:
        continue


resp_exportar_csv = entradas_usuario.exportar_csv()
if resp_exportar_csv == 1:
    exportados_csv = exercicios6.exportar_arquivo(coon,colunas_csv)
else:
    print("Exportamos outro dia")


coon.close()





