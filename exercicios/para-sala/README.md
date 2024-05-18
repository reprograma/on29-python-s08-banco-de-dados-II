# Exercício de Sala 🏫  


1. **Criação de Banco de Dados e Tabelas**:
   - Crie um script Python que crie um banco de dados SQLite chamado `escola.db`. Em seguida, crie uma tabela chamada `estudantes` com as colunas `id` (INTEGER, chave primária, autoincremento), `nome` (TEXT) e `idade` (INTEGER).

   ```python
   import sqlite3

   conn = sqlite3.connect('escola.db')
   cursor = conn.cursor()

   cursor.execute("""
   CREATE TABLE IF NOT EXISTS estudantes (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome TEXT NOT NULL,
       idade INTEGER NOT NULL
   )
   """)

   conn.commit()
   cursor.close()
   conn.close()
   ```

2. **Inserção de Dados**:
   - Escreva um script que insira três registros na tabela `estudantes`.

   ```python
   conn = sqlite3.connect('escola.db')
   cursor = conn.cursor()

   estudantes = [
       ('Alice', 21),
       ('Bob', 22),
       ('Charlie', 23)
   ]

   cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)

   conn.commit()
   cursor.close()
   conn.close()
   ```

3. **Consulta de Dados**:
   - Crie um script que selecione e exiba todos os registros da tabela `estudantes`.

   ```python
   conn = sqlite3.connect('escola.db')
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM estudantes")
   registros = cursor.fetchall()

   for registro in registros:
       print(registro)

   cursor.close()
   conn.close()
   ```

4. **Atualização de Dados**:
   - Escreva um script que atualize a idade de um estudante específico (por exemplo, mude a idade de "Bob" para 23).

   ```python
   conn = sqlite3.connect('escola.db')
   cursor = conn.cursor()

   cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))

   conn.commit()
   cursor.close()
   conn.close()
   ```

5. **Remoção de Dados**:
   - Crie um script que remova um estudante específico (por exemplo, remova "Charlie").

   ```python
   conn = sqlite3.connect('escola.db')
   cursor = conn.cursor()

   cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

   conn.commit()
   cursor.close()
   conn.close()
   ```

6. **Consulta com Condições**:
   - Escreva um script que selecione e exiba todos os estudantes cuja idade seja maior que 21.

   ```python
   conn = sqlite3.connect('escola.db')
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM estudantes WHERE idade > 21")
   registros = cursor.fetchall()

   for registro in registros:
       print(registro)

   cursor.close()
   conn.close()
   ```

#### Exercícios com CSV e Python

7. **Leitura de CSV**:
   - Crie um script que leia um arquivo CSV chamado `produtos.csv` contendo as colunas `id`, `nome` e `preco`, e exiba seu conteúdo no terminal.

   ```python
   import csv

   with open('produtos.csv', newline='', encoding='utf-8') as csvfile:
       leitor = csv.reader(csvfile)
       for linha in leitor:
           print(linha)
   ```

8. **Escrita em CSV**:
   - Escreva um script que crie um arquivo CSV chamado `funcionarios.csv` com as colunas `id`, `nome`, `departamento`.

   ```python
   import csv

   funcionarios = [
       [1, 'Ana', 'Financeiro'],
       [2, 'Carlos', 'TI'],
       [3, 'Beatriz', 'RH']
   ]

   with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
       escritor = csv.writer(csvfile)
       escritor.writerow(['id', 'nome', 'departamento'])
       escritor.writerows(funcionarios)
   ```

9. **Importação de CSV para SQLite**:
   - Crie um script que leia um arquivo CSV chamado `clientes.csv` e insira os dados em uma tabela `clientes` no banco de dados SQLite `empresa.db`. A tabela deve ter as colunas `id`, `nome`, `email`.

   ```python
   import sqlite3
   import csv

   conn = sqlite3.connect('empresa.db')
   cursor = conn.cursor()

   cursor.execute("""
   CREATE TABLE IF NOT EXISTS clientes (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome TEXT NOT NULL,
       email TEXT NOT NULL
   )
   """)

   with open('clientes.csv', newline='', encoding='utf-8') as csvfile:
       leitor = csv.reader(csvfile)
       next(leitor)  # Pular o cabeçalho
       for linha in leitor:
           cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (linha[1], linha[2]))

   conn.commit()
   cursor.close()
   conn.close()
   ```

10. **Exportação de SQLite para CSV**:
    - Escreva um script que exporte os dados da tabela `clientes` do banco de dados `empresa.db` para um arquivo CSV chamado `exportados_clientes.csv`.

    ```python
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    dados = cursor.fetchall()

    with open('exportados_clientes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(['id', 'nome', 'email'])
        escritor.writerows(dados)

    cursor.close()
    conn.close()
    ```


---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
