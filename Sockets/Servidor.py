import socket
import json

def main():
    # Configurações do servidor
    server_address = "127.0.0.1"  # Endereço do servidor (localhost)
    server_port = 8080  # Número da porta que o servidor está ouvindo

    try:
        # Cria um socket TCP/IP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Associa o socket ao endereço e porta especificados
            server_socket.bind((server_address, server_port))
            # Coloca o socket em modo de escuta
            server_socket.listen()

            print("Servidor esperando por conexões...")

            # Aceita uma conexão de um cliente e retorna um novo socket e o endereço do cliente
            client_socket, client_address = server_socket.accept()
            print("Cliente conectado:", client_address)

            # Cria um stream de leitura associado ao socket do cliente
            with client_socket, client_socket.makefile('r') as in_stream:
                # Loop para processar 5 mensagens
                for i in range(5):
                    # Lê uma linha da mensagem enviada pelo cliente e remove espaços em branco
                    user_input = in_stream.readline().strip()

                    # Desserializa a mensagem JSON em um objeto Python
                    json_object = json.loads(user_input)# transformar essa sequência de bytes em um objeto Python
                                                        # que o código possa manipular e acessar de maneira conveniente.

                    # Extrai os campos da mensagem JSON
                    nome = json_object["Nome"]
                    cpf = json_object["CPF"]
                    idade = json_object["idade"]
                    mensagem = json_object["mensagem"]

                    print()

                    # Formata e imprime a mensagem em diferentes formatos com base no valor de i
                    if i == 0:
                        print("Formato CSV:")
                        csv_message = f"Nome,CPF,idade,mensagem\n{nome},{cpf},{idade},{mensagem}"
                        print(csv_message + "\n")
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
        # Captura e imprime qualquer exceção que ocorra durante a execução do código
        print(e)

if __name__ == "__main__":
    # Chama a função main() se o script estiver sendo executado como o programa principal
    main()
