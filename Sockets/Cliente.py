import socket
import json

def main():
    # Configurações do servidor
    server_address = "127.0.0.1"  # Endereço do servidor (localhost)
    server_port = 8080  # Número da porta que o servidor está ouvindo

    try:
        # Cria uma conexão com o servidor usando o endereço e a porta especificados
        with socket.create_connection((server_address, server_port)) as client_socket:
            # Loop para enviar 5 mensagens
            for i in range(5):
                # Solicita ao usuário para inserir os dados no formato específico
                print("Digite os dados (Nome, CPF, idade, mensagem) na seguinte forma:")
                input_data = input()  # Lê a entrada do usuário
                data_parts = input_data.split(",")  # Divide a entrada em partes separadas por vírgulas
                print()  # Pula uma linha

                # Verifica se foram fornecidas exatamente 4 partes de dados
                if len(data_parts) != 4:
                    print("Formato incorreto. Certifique-se de inserir Nome, CPF, idade e mensagem separados por vírgula.")
                    continue  # Pula para a próxima iteração do loop

                # Extrai cada parte dos dados e remove espaços em branco extras
                nome = data_parts[0].strip()
                cpf = data_parts[1].strip()

                try:
                    idade = int(data_parts[2].strip())  # Converte a parte da idade em um número inteiro
                except ValueError:
                    print("Idade deve ser um número inteiro.")
                    continue  # Pula para a próxima iteração do loop se a idade não for um número

                mensagem = data_parts[3].strip()  # Extrai cada parte dos dados e remove espaços em branco extras

                # Cria um dicionário com os dados formatados
                json_message = {
                    "Nome": nome,
                    "CPF": cpf,
                    "idade": idade,
                    "mensagem": mensagem
                }

                # Serializa o dicionário em uma string JSON, codifica em bytes e envia ao servidor
                client_socket.sendall(json.dumps(json_message).encode() + b"\n")

    except Exception as e:
        # Captura e imprime qualquer exceção que ocorra durante a execução do código
        print(e)

if __name__ == "__main__":
    # Chama a função main() se o script estiver sendo executado como o programa principal
    main()
