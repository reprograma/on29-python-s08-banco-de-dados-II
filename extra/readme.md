### Conteúdo Extra: Uso de Funções Agregadas e Joins em SQLite

#### Funções Agregadas em SQLite

As funções agregadas são usadas para realizar cálculos em um conjunto de valores e retornar um único valor. Aqui estão algumas das funções agregadas mais comuns:

1. **SUM**: Retorna a soma de um conjunto de valores.
2. **AVG**: Retorna a média de um conjunto de valores.
3. **COUNT**: Retorna a contagem de valores em um conjunto.
4. **MAX**: Retorna o valor máximo de um conjunto de valores.
5. **MIN**: Retorna o valor mínimo de um conjunto de valores.

#### Exemplos de Funções Agregadas

Vamos usar uma tabela `vendas` com as seguintes colunas: `id`, `produto`, `quantidade`, `preco`.

```sql
CREATE TABLE vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL
);

INSERT INTO vendas (produto, quantidade, preco) VALUES
('Produto A', 10, 5.0),
('Produto B', 5, 10.0),
('Produto C', 2, 20.0),
('Produto A', 3, 5.0),
('Produto B', 7, 10.0);
```

##### SUM
```sql
SELECT produto, SUM(quantidade) AS total_quantidade
FROM vendas
GROUP BY produto;
```

##### AVG
```sql
SELECT produto, AVG(preco) AS preco_medio
FROM vendas
GROUP BY produto;
```

##### COUNT
```sql
SELECT COUNT(*) AS total_vendas
FROM vendas;
```

##### MAX
```sql
SELECT produto, MAX(preco) AS preco_maximo
FROM vendas
GROUP BY produto;
```

##### MIN
```sql
SELECT produto, MIN(preco) AS preco_minimo
FROM vendas
GROUP BY produto;
```

#### Joins em SQLite

Os joins são usados para combinar registros de duas ou mais tabelas com base em uma condição relacionada entre elas.

1. **INNER JOIN**: Retorna registros que têm correspondência em ambas as tabelas.
2. **LEFT JOIN (ou LEFT OUTER JOIN)**: Retorna todos os registros da tabela à esquerda e os registros correspondentes da tabela à direita. Se não houver correspondência, os resultados da tabela à direita serão NULL.
3. **RIGHT JOIN (ou RIGHT OUTER JOIN)**: Retorna todos os registros da tabela à direita e os registros correspondentes da tabela à esquerda. Se não houver correspondência, os resultados da tabela à esquerda serão NULL. *Nota: O RIGHT JOIN não é diretamente suportado pelo SQLite, mas pode ser simulado com LEFT JOIN e a troca das tabelas.*
4. **FULL JOIN (ou FULL OUTER JOIN)**: Retorna todos os registros quando há uma correspondência em uma das tabelas. *Nota: O FULL JOIN não é suportado pelo SQLite, mas pode ser simulado com a união de LEFT JOIN e RIGHT JOIN.*

##### Exemplos de Joins

Vamos usar duas tabelas: `clientes` e `pedidos`.

```sql
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

INSERT INTO clientes (nome) VALUES
('João'),
('Maria'),
('Pedro');

INSERT INTO pedidos (cliente_id, produto, quantidade) VALUES
(1, 'Produto A', 2),
(2, 'Produto B', 3),
(3, 'Produto C', 1),
(1, 'Produto D', 5);
```

##### INNER JOIN
```sql
SELECT clientes.nome, pedidos.produto, pedidos.quantidade
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;
```

##### LEFT JOIN
```sql
SELECT clientes.nome, pedidos.produto, pedidos.quantidade
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;
```

##### RIGHT JOIN (Simulado)
```sql
SELECT pedidos.produto, pedidos.quantidade, clientes.nome
FROM pedidos
LEFT JOIN clientes ON pedidos.cliente_id = clientes.id;
```

##### FULL JOIN (Simulado)
```sql
SELECT clientes.nome, pedidos.produto, pedidos.quantidade
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id
UNION
SELECT clientes.nome, pedidos.produto, pedidos.quantidade
FROM pedidos
LEFT JOIN clientes ON pedidos.cliente_id = clientes.id;
```

### Exercícios para Prática

1. **Usando Funções Agregadas**:
    - Calcule o total de quantidade vendida para cada produto.
    - Encontre o preço médio de venda para cada produto.
    - Conte o número total de vendas registradas.
    - Encontre o preço máximo e mínimo de venda para cada produto.

2. **Usando Joins**:
    - Faça uma consulta que retorne os nomes dos clientes e os produtos que compraram usando INNER JOIN.
    - Use LEFT JOIN para listar todos os clientes e seus pedidos, incluindo aqueles que não fizeram nenhum pedido.
    - Simule um RIGHT JOIN para listar todos os pedidos e os clientes correspondentes, incluindo pedidos feitos por clientes que não estão na tabela `clientes`.
    - Simule um FULL JOIN para listar todos os clientes e pedidos, mostrando todas as correspondências possíveis e os registros não correspondentes de ambas as tabelas.

### Scripts Python para Prática

#### Usando Funções Agregadas

```python
import sqlite3

conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL
);
""")

cursor.executemany("INSERT INTO vendas (produto, quantidade, preco) VALUES (?, ?, ?)", [
    ('Produto A', 10, 5.0),
    ('Produto B', 5, 10.0),
    ('Produto C', 2, 20.0),
    ('Produto A', 3, 5.0),
    ('Produto B', 7, 10.0)
])

conn.commit()

# Funções Agregadas
cursor.execute("SELECT produto, SUM(quantidade) AS total_quantidade FROM vendas GROUP BY produto")
print(cursor.fetchall())

cursor.execute("SELECT produto, AVG(preco) AS preco_medio FROM vendas GROUP BY produto")
print(cursor.fetchall())

cursor.execute("SELECT COUNT(*) AS total_vendas FROM vendas")
print(cursor.fetchall())

cursor.execute("SELECT produto, MAX(preco) AS preco_maximo FROM vendas GROUP BY produto")
print(cursor.fetchall())

cursor.execute("SELECT produto, MIN(preco) AS preco_minimo FROM vendas GROUP BY produto")
print(cursor.fetchall())

cursor.close()
conn.close()
```

#### Usando Joins

```python
import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

# Criando as tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
""")

# Inserindo dados
cursor.executemany("INSERT INTO clientes (nome) VALUES (?)", [
    ('João',),
    ('Maria',),
    ('Pedro',)
])

cursor.executemany("INSERT INTO pedidos (cliente_id, produto, quantidade) VALUES (?, ?, ?)", [
    (1, 'Produto A', 2),
    (2, 'Produto B', 3),
    (3, 'Produto C', 1),
    (1, 'Produto D', 5)
])

conn.commit()

# INNER JOIN
cursor.execute("""
SELECT clientes.nome, pedidos.produto, pedidos.quantidade
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;
""")
print(cursor.fetchall())

# LEFT JOIN
cursor.execute("""
SELECT clientes.nome, pedidos.produto, pedidos.quantidade
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;
""")
print(cursor.fetchall())

# RIGHT JOIN (Simulado)
cursor.execute("""
SELECT pedidos.produto, pedidos.quantidade, clientes.nome
FROM pedidos
LEFT JOIN clientes ON pedidos.cliente_id = clientes.id;
""")
print(cursor.fetchall())

# FULL JOIN (Simulado)
cursor.execute("""
SELECT clientes.nome, pedidos.produto, pedidos.quantidade
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id
UNION
SELECT clientes.nome, pedidos.produto, pedidos.quantidade
FROM pedidos
LEFT JOIN clientes ON pedidos.cliente_id = clientes.id;
""")
print(cursor.fetchall())

cursor.close()
conn.close()
```