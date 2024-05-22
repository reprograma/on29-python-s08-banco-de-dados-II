from funcoes import funcoes

print("Escolha qual função de banco de dados deseja utilizar")
print("1. Criação do Banco de Dados e Tabela")
print("2. Importação de Dados de um CSV")
print("3. Consulta e Exibição de Dados")
print("4. Atualização de Dados")
print("5. Remoção de Dados")
print("6. Exportação de Dados para CSV")
print("0. Encerrar")
acao = int(input("Digite a opção escolhida: "))

while True:
    if acao == 1:
        funcoes.criar_banco_dados_tabela()
        break
    elif acao == 2:
        funcoes.importar_csv()
        break
    elif acao == 3:
        funcoes.exibir_dados()
        break
    elif acao == 4:
        id = int(input("O valor de qual ID deseja alterar? "))
        valor = float(input("Qual o novo valor? "))
        funcoes.atualizar_dados(id, valor)
        break
    elif acao == 5:
        id = int(input("Qual ID deseja remover? "))
        funcoes.remover_dados(id)
        break
    elif acao == 6:
        funcoes.exportar_csv()
        break
    elif acao == 0:
        break
    else:
        print("Opção invalida!")
        continue