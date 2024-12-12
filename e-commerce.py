import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Criação das tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(255),
    data DATETIME DEFAULT CURRENT_TIMESTAMP,
    e_admin BOOLEAN
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome TEXT,
    descricao TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome VARCHAR(150),
    descricao TEXT,
    preco FLOAT,
    quantidade INTEGER,
    categoria_id INTEGER,
    data DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    usuario_id INTEGER,
    status TEXT,
    valor_do_pedido FLOAT,
    data DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Itens_do_Pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    pedidos_id INTEGER,
    produtos_id INTEGER,
    quantidade INTEGER,
    preco FLOAT,
    FOREIGN KEY (pedidos_id) REFERENCES Pedidos(id),
    FOREIGN KEY (produtos_id) REFERENCES Produtos(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Pagamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    pedidos_id INTEGER,
    pagamentos FLOAT,
    status VARCHAR(10),
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pedidos_id) REFERENCES Pedidos(id)
);
""")

conn.commit()

# Inserção de dados iniciais
cursor.execute("INSERT INTO Usuarios (nome, email, senha, e_admin) VALUES (?, ?, ?, ?)",
               ("Admin", "admin@example.com", "123456", True))

cursor.execute("INSERT INTO Categorias (nome, descricao) VALUES (?, ?)",
               ("Eletrônicos", "Dispositivos eletrônicos e gadgets"))

cursor.execute("INSERT INTO Produtos (nome, descricao, preco, quantidade, categoria_id) VALUES (?, ?, ?, ?, ?)",
               ("Smartphone", "Um smartphone moderno", 1999.99, 50, 1))

conn.commit()

# Queries de exemplo
# 1. Listar todos os usuários
print("Usuários cadastrados:")
for row in cursor.execute("SELECT * FROM Usuarios"):
    print(row)

# 2. Listar categorias
print("\nCategorias cadastradas:")
for row in cursor.execute("SELECT * FROM Categorias"):
    print(row)

# 3. Listar produtos por categoria
print("\nProdutos da categoria 'Eletrônicos':")
cursor.execute("""
SELECT Produtos.nome, Produtos.descricao, Produtos.preco 
FROM Produtos 
JOIN Categorias ON Produtos.categoria_id = Categorias.id 
WHERE Categorias.nome = ?
""", ("Eletrônicos",))
for row in cursor.fetchall():
    print(row)

# 4. Inserir um pedido
cursor.execute("INSERT INTO Pedidos (usuario_id, status, valor_do_pedido) VALUES (?, ?, ?)",
               (1, "pendente", 1999.99))
conn.commit()

print("\nPedido inserido com sucesso!")

# Fechar a conexão
conn.close()
