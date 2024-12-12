# Projeto de Banco de Dados para E-commerce

Este repositório contém o modelo de banco de dados desenvolvido para um sistema de e-commerce, incluindo tabelas para gerenciar usuários, categorias, produtos, pedidos, itens de pedido e pagamentos. Este modelo é ideal para aplicações que necessitam de uma estrutura robusta para organizar e manipular dados relacionados a compras online.

---

## **Estrutura do Banco de Dados**

### **1. Usuários (`Usuarios`)**
Tabela responsável por armazenar informações dos usuários registrados no sistema.  
**Campos principais:**
- ID único para cada usuário.
- Nome, e-mail e senha criptografada.
- Indicador de administrador.

---

### **2. Categorias (`Categorias`)**
Tabela para organizar produtos em categorias.  
**Campos principais:**
- ID único.
- Nome e descrição da categoria.

---

### **3. Produtos (`Produtos`)**
Tabela para gerenciar os produtos disponíveis para venda.  
**Campos principais:**
- ID único para cada produto.
- Nome, descrição e preço.
- Quantidade em estoque.
- Categoria associada.

---

### **4. Pedidos (`Pedidos`)**
Tabela para armazenar pedidos realizados pelos usuários.  
**Campos principais:**
- ID único para cada pedido.
- ID do usuário que realizou o pedido.
- Status do pedido e valor total.

---

### **5. Itens do Pedido (`Itens_do_Pedido`)**
Tabela para detalhar os produtos em cada pedido.  
**Campos principais:**
- ID único para cada item.
- Referência ao pedido e ao produto.
- Quantidade e preço por unidade.

---

### **6. Pagamentos (`Pagamentos`)**
Tabela para registrar informações sobre os pagamentos realizados.  
**Campos principais:**
- ID único para cada pagamento.
- ID do pedido associado.
- Valor pago, status do pagamento e data.

---

## **Como Utilizar**

Necessario ter o Python e Sqlite instalado na máquina.

1. Clone este repositório em sua máquina:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git](https://github.com/cicero12lira/e_commerce.git


