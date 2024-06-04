
def nome_db():
    db = input("Digite o nome que você deseja dar para o banco de dados, com a extenção db (nome.db):\n")
    return db

def nome_tabela():
    tabela = input("Digite o nome que você deseja dar para a tabela:\n")
    return tabela

def colunas():
    colunas = input("Digite os nome das colunas da tabela que você criou, separadas por virgula e de acordo com o exemplo: (nome text not null, idade integer not null, sobrenome text not null)\n\n")
    return colunas

def col_csv():
    
    colunas_csv = input("Digite as colunas que você deseja inserir em sua tabela separadas por vírgula (nome, idade,sobrenome):\n\n ")
    lista_col_csv = [coluna.strip() for coluna in colunas_csv.split(",")]

    tabela_csv = []

    for i in lista_col_csv:
        tabela_csv.append(i)
    
    return tabela_csv

def valores_csv(tabela_csv):

    tab_valores = []

    controle = True

    while controle:
        valores_csv = input(f"Digite os valoes para as colunas {tabela_csv}, separados por vígula, quando acabar uma linha, digite enter e escolha a opção\n\n")
        lista_valores_csv = [valor.strip() for valor in valores_csv.split(",")]
    
        if len(tabela_csv) != len(lista_valores_csv):
            print("Você inseriu uma quantidade de valores insuficientes para as colunas da tabela!\n\n")
        else:
            tab_valores.append(lista_valores_csv)
        
        opt = input("Você deseja inserir mais valores ? [1]Sim / [2]Não\n\n")
        if int(opt) != 1:
            controle = False

    return tab_valores
 

def opcoes():
    
    opt_principal = input(" O que você deseja fazer:\n\n[1] Consultar dados\n\n[2] Atualizar dados\n\n[3] Deletar dados\n\n [4] Sair do menu de opções")

    return int(opt_principal)


def atualizar_dados():

    opt1 = input("Você deseja atualizar o preço de algum livro?\n  [1] SIM [2] NÃO")

    if int(opt1) == 1:
        opt2 = input("Digite o Id  do livro que você deseja atualizar\n")
        opt3 = input("Digite o valor do preço\n")
    else:
        print("OK, vamos manter do mesmo jeito!")
    
    return opt2,opt3

def remover():
    opt1 = input("Você deseja remover algum livro?\n  [1] SIM [2] NÃO\n")

    if int(opt1) == 1:
        opt2 = input("Digite o Id do livro que você deseja remover\n")
    else:
        print("OK, vamos mater do mesmo jeito!\n")
    
    return int(opt2)


def exportar_csv():
    opt_csv = input("Você deseja exportar esses dados para um arquivo CSV? \n [1] SIm [2] NÃO\n ")

    return int(opt_csv)

