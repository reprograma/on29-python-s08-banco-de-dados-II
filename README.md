<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Tema da Aula

Turma Online X | X-end | Semana X | 202X | Professora X

### Instruções
Antes de começar, vamos organizar nosso setup.
* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)
* [Add outras intrucoes caso necessario]

### Resumo
O que veremos na aula de hoje?
* [Tema1](#tema1)
* [Tema2](#tema2)
* [Tema3](#tema3)



## Introdução ao SQLite

SQLite é um sistema de gerenciamento de banco de dados relacional (SGBD) leve, autocontido e embutido. Ele é amplamente utilizado em aplicativos que requerem um banco de dados eficiente, sem a necessidade de um servidor separado.

#### Instalando e Importando o Módulo `sqlite3`

O módulo `sqlite3` é incluído na biblioteca padrão do Python, então não é necessário instalar pacotes adicionais. Para usá-lo, basta importá-lo no seu script Python:

```python
import sqlite3
```

#### Criando e Conectando ao Banco de Dados

Para conectar a um banco de dados SQLite, usamos a função `sqlite3.connect()`. Se o banco de dados não existir, ele será criado automaticamente.

```python
# Conectando ao banco de dados (ou criando, se não existir)
conn = sqlite3.connect('meu_banco_de_dados.db')

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()
```

#### Executando Comandos SQL

A seguir, vamos aprender a executar comandos SQL básicos: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, e `JOIN`.

##### 1. Comando `SELECT`

O comando `SELECT` é usado para buscar dados no banco de dados.

```python
# Selecionando todos os registros de uma tabela
cursor.execute("SELECT * FROM minha_tabela")
resultados = cursor.fetchall()

# Exibindo os resultados
for linha in resultados:
    print(linha)
```

##### 2. Comando `INSERT`

O comando `INSERT` é usado para adicionar novos registros a uma tabela.

```python
# Inserindo um novo registro na tabela
cursor.execute("INSERT INTO minha_tabela (coluna1, coluna2) VALUES (?, ?)", (valor1, valor2))

# Salvando (commit) as mudanças
conn.commit()
```

##### 3. Comando `UPDATE`

O comando `UPDATE` é usado para modificar registros existentes.

```python
# Atualizando um registro existente
cursor.execute("UPDATE minha_tabela SET coluna1 = ? WHERE coluna2 = ?", (novo_valor1, valor2))

# Salvando as mudanças
conn.commit()
```

##### 4. Comando `DELETE`

O comando `DELETE` é usado para remover registros de uma tabela.

```python
# Removendo um registro da tabela
cursor.execute("DELETE FROM minha_tabela WHERE coluna1 = ?", (valor1,))

# Salvando as mudanças
conn.commit()
```

#### Usando `JOIN` e `LEFT JOIN`

O comando `JOIN` é utilizado para combinar registros de duas ou mais tabelas com base em uma coluna relacionada.

##### 1. Comando `JOIN`

```python
# Selecionando dados de duas tabelas relacionadas
cursor.execute("""
SELECT a.coluna1, b.coluna2
FROM tabela1 a
JOIN tabela2 b ON a.chave_estrangeira = b.id
""")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)
```

##### 2. Comando `LEFT JOIN`

O comando `LEFT JOIN` retorna todos os registros da tabela à esquerda e os registros correspondentes da tabela à direita. Se não houver correspondência, os resultados conterão `NULL`.

```python
# Selecionando dados com LEFT JOIN
cursor.execute("""
SELECT a.coluna1, b.coluna2
FROM tabela1 a
LEFT JOIN tabela2 b ON a.chave_estrangeira = b.id
""")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)
```

#### Fechando a Conexão

Após executar todos os comandos necessários, é importante fechar a conexão com o banco de dados.

```python
# Fechando o cursor e a conexão
cursor.close()
conn.close()
```

#### Exemplo Completo

Aqui está um exemplo completo que demonstra a criação de uma tabela, inserção, atualização, seleção, remoção de dados e uso de `JOIN`.

```python
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Criando uma tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Inserindo dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Bob", 25))

# Atualizando dados
cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (26, "Bob"))

# Selecionando dados
cursor.execute("SELECT * FROM usuarios")
for linha in cursor.fetchall():
    print(linha)

# Removendo dados
cursor.execute("DELETE FROM usuarios WHERE nome = ?", ("Alice",))

# Commit das mudanças
conn.commit()

# Fechando a conexão
cursor.close()
conn.close()
```

#### Conclusão

Este conteúdo apresenta uma introdução básica ao uso do SQLite com Python, cobrindo a criação de conexões, execução de comandos SQL fundamentais e manipulação de dados usando o módulo `sqlite3`. Com esses conhecimentos, você pode criar e gerenciar bancos de dados em seus projetos Python de forma eficiente.




***
### Exercícios 
* [Exercicio para sala](https://github.com/mflilian/repo-example/tree/main/exercicios/para-sala)
* [Exercicio para casa](https://github.com/mflilian/repo-example/tree/main/exercicios/para-casa)

### Material da aula 

### Links Úteis
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)


<p align="center">
Desenvolvido com :purple_heart:  
</p>

