# Sistema de Gerenciamento de Oficina Mecânica

## Descrição
Este projeto é um sistema para controle e gerenciamento de execução de ordens de serviço em uma oficina mecânica. Ele utiliza SQLite para armazenamento de dados e fornece funcionalidades para:

- Cadastro de clientes e seus veículos.
- Registro de equipes de mecânicos e suas especialidades.
- Criação e gerenciamento de ordens de serviço (OS).
- Associação de serviços e peças às ordens de serviço.
- Cálculo automático do valor total da OS.

## Estrutura do Banco de Dados

### Tabelas Principais:
- **Clientes**: Informções sobre os clientes.
- **Veiculos**: Detalhes dos veículos vinculados aos clientes.
- **Mecanicos**: Dados dos mecânicos, incluindo especialidades.
- **Equipes**: Grupos de mecânicos que trabalham juntos.
- **Servicos**: Tabela de referência para descrição e custo de mão de obra.
- **Pecas**: Informções sobre peças usadas nos reparos.
- **Ordens_Servico**: Registros das ordens de serviço, incluindo status e valores.
- **Itens_OS**: Associação entre ordens de serviço, serviços realizados e peças utilizadas.

## Funcionalidades Implementadas

1. **Cadastro Inicial**:
   - Inserção de clientes, veículos, mecânicos e equipes.
   - Registro de serviços e peças disponíveis.

2. **Gestão de Ordens de Serviço**:
   - Criação de ordens de serviço com data de emissão, status e data de conclusão.
   - Vinculação de serviços e peças a cada OS.

3. **Consultas**:
   - Listagem de clientes cadastrados.
   - Consulta de ordens de serviço e seus respectivos serviços e peças.

## Como Executar

1. Certifique-se de ter Python 3.x instalado.
2. Clone este repositório.
3. Execute o arquivo `oficina.py` para criar o banco de dados e realizar operações iniciais.
4. Confira os dados no banco através dos exemplos de consultas incluídos.

## Requisitos

- Python 3.x
- SQLite (incluído no Python padrão)

## Melhorias Futuras
- Interface gráfica para interação com o sistema.
- Relatórios automatizados de serviços e faturamento.
- Sistema de autenticação para acesso ao sistema.

---

