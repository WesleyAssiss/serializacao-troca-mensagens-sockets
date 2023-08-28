import socket
import json
from builtins import print


def main():
    server_address = "127.0.0.1"
    server_port = 8080  # Use port 8080

    try:
        with socket.create_connection((server_address, server_port)) as client_socket:
            for i in range(5):
                print("Digite os dados (Nome, CPF, idade, mensagem) na seguinte forma:")
                input_data = input()
                data_parts = input_data.split(",")
                print()
                if len(data_parts) != 4:
                    print("Formato incorreto. Certifique-se de inserir Nome, CPF, idade e mensagem separados por vírgula.")
                    continue

                nome = data_parts[0].strip()
                cpf = data_parts[1].strip()

                try:
                    idade = int(data_parts[2].strip())
                except ValueError:
                    print("Idade deve ser um número inteiro.")
                    continue

                mensagem = data_parts[3].strip()

                json_message = {
                    "Nome": nome,
                    "CPF": cpf,
                    "idade": idade,
                    "mensagem": mensagem
                }

                client_socket.sendall(json.dumps(json_message).encode() + b"\n")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
