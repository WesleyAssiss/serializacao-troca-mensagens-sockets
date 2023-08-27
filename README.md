# serializacao-troca-mensagens-sockets

Claro, aqui está uma versão resumida do `README.md`:

# Sistema de Troca de Mensagens com Serialização

Este é um sistema cliente-servidor via sockets para demonstrar diversos formatos de serialização: CSV, JSON, XML, YAML e TOML.

## Requisitos

- Java Development Kit (JDK) instalado.

## Execução

1. **Compilação:**

   Compile os arquivos `Cliente.java` e `Servidor.java`:

   ```bash
   javac org/example/Cliente.java
   javac org/example/Servidor.java
   ```

2. **Execução do Servidor:**

   Inicie o servidor:

   ```bash
   java org.example.Servidor
   ```

3. **Execução do Cliente:**

   Inicie o cliente:

   ```bash
   java org.example.Cliente
   ```

## Instruções para o Cliente

- Insira os dados do usuário (Nome, CPF, idade e mensagem) separados por vírgulas.
- Formato: Nome,CPF,idade,mensagem
- O cliente enviará em 5 formatos de serialização.

## Resultados

- O servidor exibirá os dados recebidos em cada formato.
- Resultados impressos no terminal do servidor.

## Observações

- Exemplo simples para demonstração.
- Garanta que o servidor esteja ativo antes do cliente.
- Dados manipulados em memória, não persistentes.

