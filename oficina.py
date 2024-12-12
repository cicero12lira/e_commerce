import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect("oficina.db")
cursor = conn.cursor()

# Criação das tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome VARCHAR(100),
    endereco TEXT,
    telefone VARCHAR(15)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Veiculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    placa VARCHAR(10),
    modelo VARCHAR(50),
    ano INTEGER,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Mecanicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome VARCHAR(100),
    endereco TEXT,
    especialidade VARCHAR(50)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Equipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome VARCHAR(100)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Equipe_Mecanicos (
    equipe_id INTEGER,
    mecanico_id INTEGER,
    PRIMARY KEY (equipe_id, mecanico_id),
    FOREIGN KEY (equipe_id) REFERENCES Equipes(id),
    FOREIGN KEY (mecanico_id) REFERENCES Mecanicos(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Servicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    descricao TEXT,
    valor_mao_de_obra FLOAT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Pecas (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    descricao TEXT,
    valor FLOAT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Ordens_Servico (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    numero INTEGER,
    data_emissao DATETIME DEFAULT CURRENT_TIMESTAMP,
    valor_total FLOAT,
    status VARCHAR(20),
    data_conclusao DATETIME,
    veiculo_id INTEGER,
    equipe_id INTEGER,
    FOREIGN KEY (veiculo_id) REFERENCES Veiculos(id),
    FOREIGN KEY (equipe_id) REFERENCES Equipes(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Itens_OS (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    ordem_servico_id INTEGER,
    servico_id INTEGER,
    peca_id INTEGER,
    quantidade_pecas INTEGER,
    valor_servico FLOAT,
    FOREIGN KEY (ordem_servico_id) REFERENCES Ordens_Servico(id),
    FOREIGN KEY (servico_id) REFERENCES Servicos(id),
    FOREIGN KEY (peca_id) REFERENCES Pecas(id)
);
""")

conn.commit()

# Inserção de dados iniciais
cursor.execute("INSERT INTO Clientes (nome, endereco, telefone) VALUES (?, ?, ?)",
               ("João Silva", "Rua A, 123", "99999-9999"))

cursor.execute("INSERT INTO Veiculos (placa, modelo, ano, cliente_id) VALUES (?, ?, ?, ?)",
               ("ABC1234", "Gol", 2010, 1))

cursor.execute("INSERT INTO Mecanicos (nome, endereco, especialidade) VALUES (?, ?, ?)",
               ("Carlos Oliveira", "Rua B, 456", "Motor"))

cursor.execute("INSERT INTO Equipes (nome) VALUES (?)", ("Equipe 1",))

cursor.execute("INSERT INTO Equipe_Mecanicos (equipe_id, mecanico_id) VALUES (?, ?)", (1, 1))

cursor.execute("INSERT INTO Servicos (descricao, valor_mao_de_obra) VALUES (?, ?)",
               ("Troca de óleo", 100.0))

cursor.execute("INSERT INTO Pecas (descricao, valor) VALUES (?, ?)",
               ("Filtro de óleo", 50.0))

cursor.execute("INSERT INTO Ordens_Servico (numero, valor_total, status, data_conclusao, veiculo_id, equipe_id) VALUES (?, ?, ?, ?, ?, ?)",
               (1, 150.0, "Pendente", "2024-12-15", 1, 1))

cursor.execute("INSERT INTO Itens_OS (ordem_servico_id, servico_id, peca_id, quantidade_pecas, valor_servico) VALUES (?, ?, ?, ?, ?)",
               (1, 1, 1, 1, 100.0))

conn.commit()

# Queries de exemplo
# 1. Listar clientes
print("Clientes cadastrados:")
for row in cursor.execute("SELECT * FROM Clientes"):
    print(row)

# 2. Listar ordens de serviço
print("\nOrdens de Serviço:")
for row in cursor.execute("SELECT * FROM Ordens_Servico"):
    print(row)

# 3. Listar serviços em uma ordem de serviço
print("\nServiços na Ordem de Serviço 1:")
cursor.execute("""
SELECT Servicos.descricao, Pecas.descricao, Itens_OS.quantidade_pecas, Itens_OS.valor_servico 
FROM Itens_OS 
JOIN Servicos ON Itens_OS.servico_id = Servicos.id 
JOIN Pecas ON Itens_OS.peca_id = Pecas.id 
WHERE Itens_OS.ordem_servico_id = ?
""", (1,))
for row in cursor.fetchall():
    print(row)

# Fechar a conexão
conn.close()
