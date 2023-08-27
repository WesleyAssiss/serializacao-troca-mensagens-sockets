Estrutura:

SD/
├── .idea
├── src/main/java/org.example
│   ├── Cliente.py
│   ├── Servidor.py
│   ├── resources
├──└── test/
│   ├── target
│   ├── .gitignore
│   └── pom.xml
└── README.md

```markdown
# Sistema de Troca de Mensagens com Serialização

Este é um pequeno sistema de troca de mensagens entre um cliente e um servidor via sockets, que demonstra diferentes formatos de serialização: CSV, JSON, XML, YAML e TOML.

## Requisitos

Certifique-se de ter o Java Development Kit (JDK) instalado em sua máquina.

## Executando o Sistema

### 1. Compilação

Abra um terminal na raiz do projeto (onde estão os arquivos `Cliente.java` e `Servidor.java`) e execute os seguintes comandos:

```bash
javac org/example/Cliente.java
javac org/example/Servidor.java
```

### 2. Execução do Servidor

No mesmo terminal, inicie o servidor com o seguinte comando:

```bash
java org.example.Servidor
```

O servidor ficará aguardando conexões.

### 3. Execução do Cliente

Em outro terminal, inicie o cliente com o seguinte comando:

```bash
java org.example.Cliente
```

O cliente enviará as informações para o servidor nos diferentes formatos de serialização.

## Instruções para o Cliente

- O cliente solicitará que você insira os dados do usuário (Nome, CPF, idade e mensagem) separados por vírgulas.
- Digite os dados conforme o exemplo: Nome,CPF,idade,mensagem
- O cliente repetirá o processo 5 vezes, enviando uma mensagem em cada formato de serialização.

## Resultados

- O servidor exibirá os dados recebidos em cada formato de serialização.
- Os resultados serão impressos no terminal do servidor.

## Observações

- Este é um exemplo simples para fins de demonstração.
- Certifique-se de que o servidor esteja em execução antes de iniciar o cliente.
- Os dados são manipulados em memória e não são persistentes.

```


