# Exercício de Casa 🏠 

### Integração Completa de CSV com SQLite usando Python

#### Objetivo

O objetivo deste exercício é praticar a integração de arquivos CSV com um banco de dados SQLite usando Python. Você irá criar um banco de dados, importar dados de um arquivo CSV para uma tabela, realizar operações de CRUD (Create, Read, Update, Delete) e, finalmente, exportar os dados da tabela para um novo arquivo CSV.

#### Descrição do Exercício

1. **Criação do Banco de Dados e Tabela** - [x]
    - Crie um banco de dados SQLite chamado `livraria.db`.
    - Crie uma tabela chamada `livros` com as colunas:
        - `id` (INTEGER, chave primária, autoincremento)
        - `titulo` (TEXT)
        - `autor` (TEXT)
        - `ano` (INTEGER)
        - `preco` (REAL)

2. **Importação de Dados de um CSV** - [x]
    - Crie um arquivo CSV chamado `livros.csv` com as colunas `titulo`, `autor`, `ano`, e `preco`.
    - Adicione pelo menos 5 registros no arquivo `livros.csv`.
    - Escreva um script Python que leia os dados de `livros.csv` e insira-os na tabela `livros`.

3. **Consulta e Exibição de Dados** - [x]
    - Escreva um script Python que selecione e exiba todos os registros da tabela `livros`.

4. **Atualização de Dados**
    - Escreva um script Python que atualize o preço de um livro específico (por exemplo, mude o preço do livro com `id` 1 para 29.99).

5. **Remoção de Dados**
    - Escreva um script Python que remova um livro específico da tabela (por exemplo, remova o livro com `id` 3).

6. **Exportação de Dados para CSV**
    - Escreva um script Python que exporte os dados da tabela `livros` para um novo arquivo CSV chamado `exportados_livros.csv`.


### Exemplo do arquivo livros.csv

Crie um arquivo CSV chamado `livros.csv` com o seguinte conteúdo:

```csv
titulo,autor,ano,preco
Livro A,Autor A,2020,25.99
Livro B,Autor B,2019,19.99
Livro C,Autor C,2018,29.99
Livro D,Autor D,2021,15.99
Livro E,Autor E,2022,22.99
```


#### Tarefas Adicionais

Para melhorar ainda mais suas habilidades, você pode adicionar as seguintes funcionalidades aos seus scripts:

1. **Validação de Dados**:
   - Adicione validações para garantir que os dados lidos do CSV sejam válidos antes de inseri-los no banco de dados.

2. **Manipulação de Exceções**:
   - Adicione tratamento de exceções para lidar com possíveis erros durante a leitura, inserção e atualização de dados.

3. **Interatividade**:
   - Torne seus scripts interativos, solicitando entradas do usuário para operações como inserção, atualização e remoção de dados.

#### Envio do Exercício

Após completar o exercício, deve ter os seguintes arquivos:
- `criar_banco.py`
- `importar_csv.py`
- `consultar_livros.py`
- `atualizar_livro.py`
- `remover_livro.py`
- `exportar_csv.py`
- `livros.csv`

Certifique-se de testar todos os scripts para garantir que eles funcionam corretamente antes de enviá-los.

Boa sorte!
---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
- [ ] Criei um Pull Request seguindo as orientaçoes que estao nesse [documento](https://github.com/mflilian/repo-example/blob/main/exercicios/para-casa/instrucoes-pull-request.md).
