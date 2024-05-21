
def menu():
    print("Escolha a opção desejada: ")
    print("1 - Criar do Banco de Dados e Tabela")
    print("2 - Importar dados de um CSV")
    print("3 - Consultar e exibir dados")
    print("4 - Atualizar dados")
    print("5 - Remover dados")
    print("6 - Exportar dados para CSV")
    print("0 - Sair")


def main():
    while True:
        menu()
        opt = int(input("Digite um número: "))

        if opt == 1:
            from funcoes_livraria import criar_banco
            criar_banco()
        elif opt == 2:
            from funcoes_livraria import import_csv
            import_csv()
        elif opt == 3:
            from funcoes_livraria import consulta_livros
            consulta_livros()
        if opt == 4:
            from funcoes_livraria import atualizar_livro
            atualizar_livro()
        elif opt == 5:
            from funcoes_livraria import remocao_livro
            remocao_livro()
        elif opt == 6:
            from funcoes_livraria import exportar_csv
            exportar_csv()
        elif opt == 0:
            print("Saindo do programa.")
            break
        else:
            print("Digite uma opção válida.")


main()
