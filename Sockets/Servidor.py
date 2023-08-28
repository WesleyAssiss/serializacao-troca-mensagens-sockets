import socket
import json

def main():
    server_address = "127.0.0.1"
    server_port = 8080  # Use port 8080

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((server_address, server_port))
            server_socket.listen()

            print("Servidor esperando por conexões...")

            client_socket, client_address = server_socket.accept()
            print("Cliente conectado:", client_address)

            with client_socket, client_socket.makefile('r') as in_stream:
                for i in range(5):
                    user_input = in_stream.readline().strip()

                    json_object = json.loads(user_input)

                    nome = json_object["Nome"]
                    cpf = json_object["CPF"]
                    idade = json_object["idade"]
                    mensagem = json_object["mensagem"]

                    print()

                    if i == 0:
                        print("Formato CSV:")
                        formatted_message_csv = f"{{\"Nome\":\"{nome}\", \"CPF\":\"{cpf}\", \"idade\":{idade}, \"mensagem\":\"{mensagem}\"}}"
                        print(formatted_message_csv + "\n")
                    elif i == 1:
                        print("Formato JSON:")
                        ordered_json_string = (
                            f'{{"Nome":"{nome}", "CPF":"{cpf}", "idade":{idade}, "mensagem":"{mensagem}"}}'
                        )
                        print(ordered_json_string + "\n")
                    elif i == 2:
                        print("Formato XML:")
                        xml_message = (
                            f"<dados>\n"
                            f"    <Nome>{nome}</Nome>\n"
                            f"    <CPF>{cpf}</CPF>\n"
                            f"    <idade>{idade}</idade>\n"
                            f"    <mensagem>{mensagem}</mensagem>\n"
                            f"</dados>"
                        )
                        print(xml_message + "\n")
                    elif i == 3:
                        print("Formato YAML:")
                        yaml_message = (
                            f"Nome: {nome}\n"
                            f"CPF: '{cpf}'\n"
                            f"idade: {idade}\n"
                            f"mensagem: \"{mensagem}\""
                        )
                        print(yaml_message + "\n")
                    elif i == 4:
                        print("Formato TOML:")
                        toml_message = (
                            f"Nome = \"{nome}\"\n"
                            f"CPF = \"{cpf}\"\n"
                            f"idade = {idade}\n"
                            f"mensagem = \"{mensagem}\""
                        )
                        print(toml_message + "\n")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
